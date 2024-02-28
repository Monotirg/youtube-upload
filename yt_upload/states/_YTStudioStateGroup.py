
from .base import YTModelField, YTPageStateGroup
from ..models import Video
from ..pages import YTStudioPage


class YTStudioStateGroup(YTPageStateGroup):
    __yt_page__ = YTStudioPage
    __yt_model__ = Video
    
    load_page = YTModelField(always=True,log_message="Load page https://studio.youtube.com/")
    input_video = YTModelField("video_path", log_message="Upload video by path")
