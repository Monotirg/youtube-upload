
from .base import YTModelField, YTPageStateGroup
from ..models import Video
from ..pages import YTVisibilityPage



class YTVisibilityStateGroup(YTPageStateGroup):
    __yt_page__ = YTVisibilityPage
    __yt_model__ = Video

    input_visibility = YTModelField("visibility", log_message="Set visibility")
    input_schedule = YTModelField("schedule", log_message="Select schedule")
    verify_upload_video = YTModelField(always=True, log_message="Verify upload video")
    press_save = YTModelField(always=True, log_message="Save video on YouTube Channel")
    press_close = YTModelField(always=True, log_message="Video uploaded successfully")
