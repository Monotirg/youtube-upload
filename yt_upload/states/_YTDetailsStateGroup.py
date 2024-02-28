
from .base import YTModelField, YTPageStateGroup
from ..models import Video
from ..pages import YTDetailsPage


class YTDetailsStateGroup(YTPageStateGroup):
    __yt_page__ = YTDetailsPage
    __yt_model__ = Video
    
    input_title = YTModelField("title", log_message="Input video title")
    input_description = YTModelField("description", log_message="Input video description")
    input_thumbnail = YTModelField("thumbnail", log_message="Upload video thumbnail")
    input_playlist = YTModelField("playlist", log_message="Select video playlists")
    input_made_for_kids = YTModelField("made_for_kids", log_message="Set made for kids")
    input_age_restriction = YTModelField("age_restriction", log_message="Set age restriction")
    press_show_more = YTModelField(always=True, log_message="Show additional YouTube Settings")
    set_contains_paid_promotion = YTModelField("contains_paid_promotion", log_message="Set contains paid promotion")
    set_allow_automatic_chapters_and_key = YTModelField("allow_automatic_chapters_and_key", log_message="Set contains allow automatic chapters and key")
    set_allow_automatic_places = YTModelField("allow_automatic_places", log_message="Set allow automatic places")
    set_allow_automatic_concepts = YTModelField("allow_automatic_concepts", log_message="Set allow automatic concepts")
    input_tags = YTModelField("tags", log_message="Input video tags")
    input_video_language = YTModelField("video_language", log_message="Select video language")
    input_caption_certification = YTModelField("caption_certification", log_message="Select video caption certification")
    input_recording_date = YTModelField("recording_date", log_message="Select recording date")
    input_video_location = YTModelField("video_location", log_message="Input video location")
    input_license = YTModelField("license", log_message="Select video license")
    set_allow_embedding = YTModelField("allow_embedding", log_message="Set allow embedding")
    set_publish_to_subscriptions_feed = YTModelField("publish_to_subscriptions_feed", log_message="Set publish to subsription feed")
    input_remixing_only_audio = YTModelField("allow_only_audio_remixing", log_message="Set allow only audio remixing")
    input_category = YTModelField("category", log_message="Select video category")
    input_education_type = YTModelField("education_type", log_message="Select education type")
    input_education_problems = YTModelField("education_problems", log_message="Input education problems")
    input_education_academic_system = YTModelField("education_academic_system", log_message="Select education academic system")
    input_education_level = YTModelField("education_level", log_message="Select education level")
    input_education_exam = YTModelField("education_exam", log_message="Select education exam")
    input_game_title = YTModelField("game_title", log_message="Input game title")
    input_comment_and_ratings = YTModelField("show_comments", log_message="Set comment and ratings")
    input_comments_moderation = YTModelField("comment_moderation", log_message="Select comment moderation")
    input_sort_by = YTModelField("sort_by", log_message="Select sort by")
    set_show_viewers_like = YTModelField("show_viewer_like", log_message="Set show viewer like")
    press_next = YTModelField(always=True, repeat=3, log_message="Starting YouTube visibilities settings")
