"""The vision pipeline abstraction helps chain image processing operations as sequence of steps. Each step consumes and produces a `FrameSet` which typically contains a source image and derivative metadata and images.
"""

import logging
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Union, cast

import cv2
import imageio
import numpy as np
from PIL import Image
from pydantic import BaseModel

from landingai.common import ClassificationPrediction, Prediction
from landingai.notebook_utils import is_running_in_notebook
from landingai.predict import Predictor
from landingai.storage.data_access import fetch_from_uri
from landingai.visualize import overlay_predictions

_LOGGER = logging.getLogger(__name__)


class Frame(BaseModel):
    """A Frame stores a main image, its metadata and potentially other derived images. This class will be mostly used internally by the FrameSet clase. A pipeline will `FrameSet` since it is more general and a can also keep new `Frames` extracted from existing ones"""

    image: Image.Image
    """Main image generated typically at the beginning of a pipeline"""

    other_images: Dict[str, Image.Image] = {}
    """Other derivative images associated with this the main image. For example: `FrameSet.overlay_predictions` will store the resulting image on `Frame.other_images["overlay"]"""

    predictions: List[ClassificationPrediction] = []
    """List of predictions for the main image"""

    metadata: Dict[str, Any] = {}
    """An optional collection of metadata"""

    def run_predict(self, predictor: Predictor) -> "Frame":
        """Run a cloud inference model
        Parameters
        ----------
        predictor: the model to be invoked.
        """
        self.predictions = predictor.predict(np.asarray(self.image))  # type: ignore
        return self

    def to_numpy_array(self, image_src: str = "") -> np.ndarray:
        """Return a numpy array using RGB channel ordering. If this array is passed to OpenCV, you will need to convert it to BGR

        Parameters
        ----------
        image_src : if empty the source image will be converted. Otherwise the image will be selected from `other_images`
        """
        img = self.image if image_src == "" else self.other_images[image_src]
        return np.asarray(img)

    class Config:
        arbitrary_types_allowed = True


class FrameSet(BaseModel):
    """A FrameSet is a collection of frames (in order). Typically a FrameSet will include a single image but there are circumstances where other images will be extracted from the initial one. For example: we may want to identify vehicles on an initial image and then extract sub-images for each of the vehicles."""

    frames: List[Frame] = []  # Start with empty frame set

    # @classmethod
    # def from_frameset_list(cls, list: List["FrameSet"] = None) -> "FrameSet":
    #     return cls(frames=list)

    @classmethod
    def from_image(
        cls, uri: str, metadata: Optional[Dict[str, Any]] = {}
    ) -> "FrameSet":
        """Creates a FrameSet from an image file

        Parameters
        ----------
        uri : URI to file (local or remote)

        Returns
        -------
        FrameSet : New FrameSet containing a single image
        """

        im = Image.open(str(fetch_from_uri(uri)))
        return cls(frames=[Frame(image=im, metadata=metadata)])

    @classmethod
    def from_array(cls, array: np.ndarray, is_bgr: bool = True) -> "FrameSet":
        """Creates a FrameSet from a image encode as ndarray

        Parameters
        ----------
        array : np.ndarray
            Image
        is_bgr : bool, optional
            Assume OpenCV's BGR channel ordering? Defaults to True

        Returns
        -------
        FrameSet
        """
        # TODO: Make is_bgr and enum and support grayscale, rgba (what can PIL autodetect?)
        if is_bgr:
            array = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(array)
        return cls(frames=[Frame(image=im)])

    # TODO: Is it worth to emulate a full container? - https://docs.python.org/3/reference/datamodel.html#emulating-container-types
    def __getitem__(self, key: int) -> Frame:
        return self.frames[key]

    def _repr_pretty_(self, pp, cycle) -> str:  # type: ignore
        # Enable a pretty output on Jupiter notebooks `Display()` function
        return str(
            pp.text(
                self.json(
                    # exclude={"frames": {"__all__": {"image", "other_images"}}},
                    indent=2
                )
            )
        )

    def is_empty(self) -> bool:
        """Check if the FrameSet is empty
        Returns
        -------
        bool
            True if the are no Frames on the FrameSet
        """
        return not self.frames  # True if the list is empty

    def run_predict(self, predictor: Predictor) -> "FrameSet":
        """Run a cloud inference model
        Parameters
        ----------
        predictor: the model to be invoked.
        """

        for frame in self.frames:
            frame.predictions = predictor.predict(np.asarray(frame.image))  # type: ignore
        return self

    def overlay_predictions(
        self, options: Optional[Dict[str, Any]] = None
    ) -> "FrameSet":  # TODO: Optional where to store
        for frame in self.frames:
            frame.other_images["overlay"] = overlay_predictions(
                cast(List[Prediction], frame.predictions), frame.image, options
            )
        return self

    def resize(
        self, width: Union[int, None] = None, height: Union[int, None] = None
    ) -> "FrameSet":  # TODO: Optional where to store
        """Returns a resized copy of this image. If width or height is missing the resize will preserve the aspect ratio
        Parameters
        ----------
        width: The requested width in pixels.
        height: The requested width in pixels.
        """
        if width is None and height is None:  # No resize needed
            return self
        for frame in self.frames:
            # Compute the final dimensions on the first image
            if width is None:
                width = int(height * float(frame.image.size[0] / frame.image.size[1]))  # type: ignore
            if height is None:
                height = int(width * float(frame.image.size[1] / frame.image.size[0]))
            frame.image = frame.image.resize((width, height))
        return self

    def downsize(
        self, width: Union[int, None] = None, height: Union[int, None] = None
    ) -> "FrameSet":  # TODO: Optional where to store
        """Resize only if the image is larger than the expected dimensions,
        Parameters
        ----------
        width: The requested width in pixels.
        height: The requested width in pixels.
        """
        if width is None and height is None:  # No resize needed
            return self
        for frame in self.frames:
            # Compute the final dimensions on the first image
            if width is None:
                width = int(height * float(frame.image.size[0] / frame.image.size[1]))  # type: ignore
            if height is None:
                height = int(width * float(frame.image.size[1] / frame.image.size[0]))
            if frame.image.size[0] > width or frame.image.size[1] > height:
                frame.image = frame.image.resize((width, height))
        return self

    def save_image(self, filename_prefix: str, image_src: str = "") -> "FrameSet":
        """Save all the images on the FrameSet to disk (as PNG)

        Parameters
        ----------
        filename_prefix : path and name prefix for the image file
        image_src : if empty the source image will be saved. Otherwise the image will be selected from `other_images`
        """
        timestamp = datetime.now().strftime(
            "%Y%m%d-%H%M%S"
        )  # TODO saving faster than 1 sec will cause image overwrite
        c = 0
        for frame in self.frames:
            img = frame.image if image_src == "" else frame.other_images[image_src]
            img.save(f"{filename_prefix}_{timestamp}_{image_src}_{c}.png", format="PNG")
            c += 1
        return self

    def save_video(
        self,
        video_file_path: str,
        video_fps: Optional[int] = None,
        video_length_sec: Optional[float] = None,
        image_src: str = "",
    ) -> "FrameSet":
        """Save the FrameSet as an mp4 video file. The following example, shows to use save_video to save a clip from a live RTSP source.
        ```python
            video_len_sec=10
            fps=4
            img_src = NetworkedCamera(stream_url, fps=fps)
            frs = FrameSet()
            for i,frame in enumerate(img_src):
                if i>=video_len_sec*fps: # Limit capture time
                    break
                frs.extend(frame)
            frs.save_video("sample_images/test.mp4",video_fps=fps)
        ```

        Parameters
        ----------
        video_file_path : str
            Path and filename with extension of the video file
        video_fps : Optional[int]
            The number of frames per second for the output video file.
            Either the `video_fps` or `video_length_sec` should be provided to assemble the video. if none of the two are provided, the method will try to set a "reasonable" value.
        video_length_sec : Optional[float]
            The total number of seconds for the output video file.
            Either the `video_fps` or `video_length_sec` should be provided to assemble the video. if none of the two are provided, the method will try to set a "reasonable" value.
        image_src : str, optional
            if empty the source image will be used. Otherwise the image will be selected from `other_images`
        """
        if not video_file_path.lower().endswith(".mp4"):
            raise NotImplementedError("Only .mp4 is supported")
        total_frames = len(self.frames)
        if total_frames == 0:
            return self

        if video_fps is not None and video_length_sec is not None:
            raise ValueError(
                "The 'video_fps' and 'video_length_sec' arguments cannot be set at the same time"
            )

        # Try to tune FPS based on parameters or pick a reasonable number. The goal is to produce a video that last a a couple of seconds even when there are few frames. OpenCV will silently fail and not create a file if the resulting fps is less than 1
        if video_length_sec is not None and video_length_sec <= total_frames:
            video_fps = int(total_frames / video_length_sec)
        elif video_fps is None:
            video_fps = min(2, total_frames)

        writer = imageio.get_writer(video_file_path, fps=video_fps)
        for fr in self.frames:
            writer.append_data(fr.to_numpy_array(image_src))
        writer.close()

        # TODO: Future delete if we get out of OpenCV
        # Previous implementation with OpenCV that required code guessing and did not work on windows because of wurlitzer (an alternative will be https://github.com/greg-hellings/stream-redirect)
        # # All images should have the same shape as it's from the same video file
        # img_shape = self.frames[0].image.size
        # # Find a suitable coded that it is installed on the system. H264/avc1 is preferred, see https://discuss.streamlit.io/t/st-video-doesnt-show-opencv-generated-mp4/3193/4

        # codecs = [
        #     cv2.VideoWriter_fourcc(*"avc1"),  # type: ignore
        #     cv2.VideoWriter_fourcc(*"hev1"),  # type: ignore
        #     cv2.VideoWriter_fourcc(*"mp4v"),  # type: ignore
        #     cv2.VideoWriter_fourcc(*"xvid"),  # type: ignore
        #     -1,  # This forces OpenCV to dump the list of codecs
        # ]
        # for fourcc in codecs:
        #     with pipes() as (out, err):
        #         video = cv2.VideoWriter(video_file_path, fourcc, video_fps, img_shape)
        #     stderr = err.read()
        #     # Print OpenCV output to help customer's understand what is going on
        #     print(out.read())
        #     print(stderr)
        #     if "is not" not in stderr:  # Found a working codec
        #         break
        # if fourcc == -1 or not video.isOpened():
        #     raise Exception(
        #         f"Could not find a suitable codec to save {video_file_path}"
        #     )
        # for fr in self.frames:
        #     video.write(cv2.cvtColor(fr.to_numpy_array(image_src), cv2.COLOR_RGB2BGR))
        # video.release()
        return self

    def show_image(
        self, image_src: str = "", clear_nb_cell: bool = False
    ) -> "FrameSet":
        """Open an a window and display all the images.
        Parameters
        ----------
        image_src: if empty the source image will be displayed. Otherwise the image will be selected from `other_images`
        """
        # TODO: Should show be a end leaf?
        # Check if we are on a notebook context
        if is_running_in_notebook():
            from IPython import display

            for frame in self.frames:
                if clear_nb_cell:
                    display.clear_output(wait=True)
                if image_src == "":
                    display.display(frame.image)
                else:
                    display.display(frame.other_images[image_src])
        else:
            # Use PIL's implementation
            for frame in self.frames:
                if image_src == "":
                    frame.image.show()
                else:
                    frame.other_images[image_src].show()

        # # TODO: Implement image stacking when we have multiple frames (https://answers.opencv.org/question/175912/how-to-display-multiple-images-in-one-window/)
        # """Open an OpenCV window and display all the images. This call will stop the execution until a key is pressed.
        # Parameters
        # ----------
        # image_src: if empty the source image will be displayed. Otherwise the image will be selected from `other_images`
        # """
        # # OpenCV is full of issues when it comes to displaying windows (see https://stackoverflow.com/questions/6116564/destroywindow-does-not-close-window-on-mac-using-python-and-opencv)
        # cv2.namedWindow("image")
        # cv2.startWindowThread()
        # if image_src == "":
        #     img = cv2.cvtColor(np.asarray(self.frames[0].image), cv2.COLOR_BGR2RGB)
        # else:
        #     img = cv2.cvtColor(np.asarray(self.frames[0].other_images[image_src]), cv2.COLOR_BGR2RGB)
        # cv2.imshow("Landing AI - Press any key to exit", img)
        # cv2.waitKey(0) # close window when a key press is detected
        # cv2.waitKey(1)
        # cv2.destroyWindow('image')
        # for i in range (1,5):
        #     cv2.waitKey(1)

        return self

    def extend(self, frs: "FrameSet") -> "FrameSet":
        """Add a all the Frames from `frs` into this FrameSet

        Parameters
        ----------
        frs : FrameSet
            Framerset to be added at the end of the current one

        Returns
        -------
        FrameSet
        """
        self.frames.extend(frs.frames)
        return self

    def apply(self, function: Callable[[Frame], Frame] = lambda f: f) -> "FrameSet":
        """Apply a function to all frames

        Parameters
        ----------
        function: lambda function that takes individual frames and returned an updated frame
        """
        for i in range(len(self.frames)):
            self.frames[i] = function(self.frames[i])
        return self

    def filter(self, function: Callable[[Frame], bool] = lambda f: True) -> "FrameSet":
        """Evaluate a function on every frame and keep or remove

        Parameters
        ----------
        function : lambda function that gets invoked on every Frame. If it returns False, the Frame will be deleted
        """
        for i in reversed(
            range(0, len(self.frames))
        ):  # Traverse in reverse so we can delete
            if not function(self.frames[i]):
                self.frames.pop(i)
        return self

    class Config:
        # Add some encoders to prevent large structures from being printed
        json_encoders = {
            np.ndarray: lambda a: f"<np.ndarray: {a.shape}>",
            Image.Image: lambda i: f"<Image.Image: {i.size}>",
        }
