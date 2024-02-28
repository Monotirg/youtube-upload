import os
import datetime as dt

from typing import Optional
from pymediainfo import MediaInfo
from pydantic import field_validator
from pydantic import BaseModel, ValidationInfo, ConfigDict

from ..typing import *
from ..utils import to_abs_path
from ..exceptions import YTVideoError
from ..constants.licenses import YT_LICENSES
from ..constants.sort_by import YT_ALL_SORT_BY
from ..constants.languages import YT_LANGUAGES
from ..constants.visibilities import YT_VISIBILITIES
from ..constants.education_types import YT_EDUCATION_TYPES
from ..constants.comment_moderations import YT_COMMENT_MODERATIONS
from ..constants.formats import YT_VIDEO_FORMATS, YT_THUMBNAIL_EXT
from ..constants.categories import YT_CATEGORIES, EDUCATION, GAMING
from ..constants.caption_certifications import YT_CAPTION_CERTIFICATIONS
from ..constants.education_acamedic_systems import YT_EDUCATION_ACADEMIC_SYSTEMS


FORMAT_DATE_ERROR = r"%Y-%m-%d %H:%M"


class YTModel: ...


class Video(BaseModel, YTModel):
    video_path: str 
    title: str
    made_for_kids: bool
    category: YT_CATEGORY
    visibility: YT_VISIBILITY
    description: Optional[str] = None 
    age_restriction: Optional[bool] = None
    thumbnail: Optional[str] = None
    playlist: Optional[list[str]] = None
    tags: Optional[list[str]] = None
    contains_paid_promotion: Optional[bool] = None
    allow_automatic_chapters_and_key: Optional[bool] = None
    allow_automatic_places: Optional[bool] = None
    allow_automatic_concepts: Optional[bool] = None
    allow_embedding: Optional[bool] = None
    publish_to_subscriptions_feed: Optional[bool] = None
    show_viewer_like: Optional[bool] = None
    allow_only_audio_remixing: Optional[bool] = None
    video_language: Optional[YT_LANGUAGE] = None
    caption_certification: Optional[YT_CAPTION_CERTIFICATION] = None
    recording_date: Optional[dt.date] = None
    video_location: Optional[str] = None
    license: Optional[YT_LICENSE] = None
    game_title: Optional[str] = None
    education_type: Optional[YT_EDUCATION_TYPE] = None
    education_academic_system: Optional[str] = None
    education_problems: Optional[list[tuple[dt.timedelta, str]]] = None
    education_level: Optional[YT_EDUCATION_LEVEL] = None
    education_exam: Optional[YT_EDUCATION_EXAM] = None
    show_comments: Optional[bool] = None
    comment_moderation: Optional[YT_COMMENT_MODERATION] = None
    sort_by: Optional[YT_SORT_BY] = None
    schedule: Optional[dt.datetime] = None
    
    model_config = ConfigDict(validate_assignment=True)
    
    @field_validator("video_path")
    @classmethod
    def validate_video_path(
        cls,
        video_path: str
    ):
        video_path = to_abs_path(video_path)
        _, ext = os.path.splitext(video_path)

        if ext not in YT_VIDEO_FORMATS:
            video_formats = "\n".join([f"{i}. {v}" for i, v in enumerate(YT_VIDEO_FORMATS, start=1)])
            raise YTVideoError(f"Not supported YouTube video format '{ext}', "
                               f"the following YouTube video formats are available:\n{video_formats}")

        return video_path

    @field_validator("category")
    @classmethod
    def validate_category(cls, category: str) -> str:
        if category not in YT_CATEGORIES:
            categories = "\n".join([f"{i}. {c}" for i, c in enumerate(YT_CATEGORIES, start=1)])
            msg = (f"Category '{category}' not found in YouTube categories, "
                   f"the following YouTube categories are available:\n{categories}")
            raise YTVideoError(msg)

        return category

    @field_validator("visibility")
    @classmethod
    def validate_visibility(cls, visibility: str) -> str:
        if visibility not in YT_VISIBILITIES:
            visibilities = "\n".join([f"{i}. {v}" for i, v in enumerate(YT_VISIBILITIES, start=1)])
            msg = (f"Visibility '{visibility}' not found in YouTube visibilities, "
                   f"the following YouTube visibilities are available:\n{visibilities}")
            raise YTVideoError(msg)
        
        return visibility

    @field_validator("age_restriction")
    @classmethod
    def validate_age_restriction(
        cls, 
        age_restriction: str, 
        info: ValidationInfo
    ) -> str:
        if info.data["made_for_kids"]:
            msg = ("Cannot set age_restriction if the video is set to made for kids, "
                   "set made_for_kids = False.")
            raise YTVideoError(msg)
        
        return age_restriction
    
    @field_validator("thumbnail")
    @classmethod
    def validate_thumbnail(cls, thumbnail: str) -> str:
        thumbnail = to_abs_path(thumbnail)
        _, ext = os.path.splitext(thumbnail)

        if ext not in YT_THUMBNAIL_EXT:
            thumbnail_formats = "\n".join([
                f"{i}. {v}" 
                for i, v in enumerate(YT_THUMBNAIL_EXT, start=1)
            ])
            msg = (f"Not supported thumbnail image format '{ext}', "
                   f"the following thumbnail image formats are available:\n{thumbnail_formats}")
            raise YTVideoError(msg)

        size = os.path.getsize(thumbnail) >> 20
        
        if size > 2:
            kb = size << 10
            kb = f"{kb:02}"[:2]
            msg = (f"Thumbnail file size {thumbnail}: {size}.{kb} mb, "
                   f"thumbnail file size must be less than 2 mb.")
            raise YTVideoError(msg)

        return thumbnail

    @field_validator("allow_automatic_places")
    @classmethod
    def validate_allow_automatic_places(
        cls, 
        allow_automatic_places: bool,
        info: ValidationInfo
        ) -> bool:
        if info.data['made_for_kids']:
            msg = ("Cannot set allow_automatic_places if the video is set to made for kids, "
                   "set made_for_kids = False.")
            raise YTVideoError(msg)
        
        return allow_automatic_places

    @field_validator("video_language")
    @classmethod
    def validate_video_language(cls, video_language: str) -> str:
        if video_language not in YT_LANGUAGES:
            languages = "\n".join([f"{i}. {c}" for i, c in enumerate(YT_LANGUAGES, start=1)])
            msg = (f"Language '{video_language}' not found in YouTube languages, "
                   f"the following YouTube languages are available:\n{languages}")
            raise YTVideoError(msg)

        return video_language

    @field_validator("caption_certification")
    @classmethod
    def validate_caption_certification(
        cls, 
        caption_certification: str
    ) -> str:
        if caption_certification not in YT_CAPTION_CERTIFICATIONS:
            certifications = "\n".join([f"{i}. {c}" for i, c in enumerate(YT_CAPTION_CERTIFICATIONS, start=1)])
            msg = (f"Caption certification '{caption_certification}' not found in YouTube caption certifications, "
                   f"the following YouTube caption certifications are available:\n{certifications}")
            raise YTVideoError(msg)

        return caption_certification

    @field_validator("recording_date")
    @classmethod
    def validate_recording_date(cls, recording_date: dt.date) -> dt.date:
        if recording_date > dt.datetime.now().date():
            msg = (f"Invalid recording date '{recording_date.strftime(FORMAT_DATE_ERROR)}', "
                   f"the recording date must be earlier then today.")
            raise YTVideoError(msg)

        return recording_date

    @field_validator("license")
    @classmethod
    def validate_license(cls, license: str) -> str:
        if license not in YT_LICENSES:
            licenses = "\n".join([f"{i}. {c}" for i, c in enumerate(YT_LICENSES, start=1)])
            msg = (f"License '{license}' not found in YouTube license, "
                   f"the following YouTube licenses are available:\n{licenses}.")
            raise YTVideoError(msg)

        return license

    @field_validator("game_title")
    @classmethod
    def validate_game_title(
        cls, 
        game_title: str, 
        info: ValidationInfo
    ):
        if game_title is None:
            return None
        
        if info.data['category'] != GAMING:
            msg = (f"Cannot set game_title if the video category is '{info.data['category']}', "
                   f"set category = '{GAMING}'.")
            raise YTVideoError(msg)
        
        return game_title

    @field_validator("education_type")
    @classmethod
    def validate_education_type(
            cls,
            education_type: str,
            info: ValidationInfo
    ) -> str:
        if info.data['category'] != EDUCATION:
            msg = (f"Cannot set education_type if the video category is '{info.data['category']}', "
                   f"set category = '{EDUCATION}'.")
            raise YTVideoError(msg)

        if education_type not in YT_EDUCATION_TYPES:
            types = "\n".join([f"{i}. {v}" for i, v in enumerate(YT_EDUCATION_TYPES, start=1)])
            msg = (f"Education type '{education_type}' is not found in YouTube educations types, "
                   f"following education types are available: {types}")
            raise YTVideoError(msg)
        
        return education_type

    @field_validator("education_academic_system")
    @classmethod
    def validate_education_academic_system(
            cls,
            education_academic_system: str,
            info: ValidationInfo
    ) -> str:
        if info.data['category'] != EDUCATION:
            msg = (f"Cannot set education_academic_system if the video category is '{info.data['category']}', "
                   f"set category = '{EDUCATION}'.")
            raise YTVideoError(msg)

        if education_academic_system not in YT_EDUCATION_ACADEMIC_SYSTEMS:
            education_systems = "\n".join([f"{i}. {v}" for i, v in enumerate(YT_EDUCATION_ACADEMIC_SYSTEMS, start=1)])
            msg = (f"Academic system '{education_academic_system}' is not found in YouTube academic systems, "
                   f"following academic systems are available:\n{education_systems}")
            raise YTVideoError(msg)

        return education_academic_system

    @field_validator("education_problems")
    @classmethod
    def validate_education_problems(
        cls, 
        education_problems: list[str],
        info: ValidationInfo
    ):
        if info.data['category'] != EDUCATION:
            msg = (f"Cannot set education_problems if the video category is '{info.data['category']}', "
                   f"set category = '{EDUCATION}'.")
            raise YTVideoError(msg)
        
        if len(education_problems) == 1:
            return education_problems
        
        video = MediaInfo.parse(info.data['video_path'])
        video_duration = video.tracks[0].duration // 1000.0
        
        if video_duration < education_problems[0][0].seconds:
            msg = (f"Invalid timestamps '{education_problems[0][0]}', "
                   f"it should be less than the video duration {video_duration}")
            raise YTVideoError(msg)

        for i in range(1, len(education_problems)):
            if video_duration < education_problems[i][0].seconds:
                msg = (f"Invalid timestamps '{education_problems[i][0]}', "
                       f"it should be less than the video duration {video_duration}")
                raise YTVideoError(msg)
            
            if education_problems[i][0] < education_problems[i - 1][0]:
                msg = (f"Invalid timestamp order, "
                       f"after '{education_problems[i-1][0]}' the next one is '{education_problems[i][0]}'.")
                raise YTVideoError(msg)
         
        return education_problems

    @field_validator("education_level")
    @classmethod
    def validate_education_level(
            cls,
            education_level: str,
            info: ValidationInfo
    ) -> str:
        if info.data['category'] != EDUCATION:
            msg = (f"Cannot set education_level if the video category is '{info.data['category']}', "
                   f"set category = '{EDUCATION}'.")
            raise YTVideoError(msg)
       
        return education_level

    @field_validator("education_exam")
    @classmethod
    def validate_education_exam(
        cls,
        education_exam: str,
        info: ValidationInfo
    ):
        if info.data['category'] != EDUCATION:
            msg = (f"Cannot set education_exam if the video category is '{info.data['category']}', "
                   f"set category = '{EDUCATION}'.")
            raise YTVideoError(msg)
        
        if info.data["education_academic_system"] is None:
            msg = f"Cannot set education_exam if education_academic_system = None"
            raise YTVideoError(msg)
        
        return education_exam

    @field_validator("comment_moderation")
    @classmethod
    def validate_comment_moderation(
            cls,
            comment_moderation: str,
            info: ValidationInfo
    ) -> str:
        if not info.data['show_comments']:
            msg = f"Cannot set comment_moderation if show_comments=False."
            raise YTVideoError(msg)
        
        if comment_moderation not in YT_COMMENT_MODERATIONS:
            comment_moderations = "\n".join([f"{i}. {v}" for i, v in enumerate(YT_COMMENT_MODERATIONS, start=1)])
            msg = (f"Comment moderation '{comment_moderation}' is not available on YouTube, "
                   f"following comment moderations are available:\n{comment_moderations}")
        
            raise YTVideoError(msg)
        
        return comment_moderation

    @field_validator("sort_by")
    @classmethod
    def validate_sort_by(
            cls,
            sort_by: str
    ) -> str:
        if sort_by not in YT_ALL_SORT_BY:
            sorted_types = "\n".join([f"{i}. {v}" for i, v in enumerate(YT_SORT_BY, start=1)])
            msg = (f"Video format '{sort_by}' is not available on YouTube, "
                   f"following video formats are available:\n{sorted_types}")
            
            raise YTVideoError(msg)
        
        return sort_by

    @field_validator("schedule")
    def validate_schedule(cls, schedule: dt.datetime) -> dt.datetime:
        
        if schedule < dt.datetime.now() + dt.timedelta(minutes=5):
            msg = (f"Invalid schedule date '{schedule.strftime(FORMAT_DATE_ERROR)}', "
                   f"the schedule date must be greater than the current date + 5 minutes.")
            raise YTVideoError(msg)
        
        if schedule >= dt.datetime.now() + dt.timedelta(days=754):
            msg = (f"Invalid schedule date '{schedule.strftime(FORMAT_DATE_ERROR)}', "
                   f"the schedule date must be less than the current date + 754 days.")
            raise YTVideoError(msg)
        
        return schedule
