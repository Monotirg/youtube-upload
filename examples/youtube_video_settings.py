import asyncio
import datetime as dt
import yt_upload as yt 


async def main():
    channel = yt.Channel(
        user_data_dir="User Data",
        profile="Profile 1",
        cookies_path="cookies.json"
    )
    video = yt.Video(
        video_path="video.mp4",
        title="Funny video",
        description="Funny video about math #math",
        made_for_kids=False,
        category=yt.category.EDUCATION,
        visibility=yt.visibility.PUBLIC,
        age_restriction=True,
        thumbnail="thumbnail.png",
        playlist=["math", ],
        tags=["math"],
        contains_paid_promotion=True,
        allow_automatic_chapters_and_key=False,
        allow_automatic_places=True,
        allow_automatic_concepts=False,
        allow_embedding=True,
        publish_to_subscriptions_feed=True,
        show_viewer_like=True,
        allow_only_audio_remixing=True,
        video_language=yt.language.ENGLISH,
        caption_certification=yt.caption_certification.CONTENT_HAS_NOT_AIRED,
        recording_date=dt.date(2023, 10, 10),
        video_location="Los Angeles",
        license=yt.licence.STANDARD_YOUTUBE,
        education_type=yt.education_type.LECTURE,
        education_academic_system=yt.education_academic_system.UNITED_STATES,
        education_problems=[
            (dt.timedelta(seconds=5), "derivative"),
            (dt.timedelta(minutes=3, seconds=2), "integral")
        ],
        education_level="College",
        education_exam="SAT Math",
        show_comments=True,
        comment_moderation=yt.comment_moderation.HOLD_ALL,
        sort_by=yt.sort_by.NEWEST,
        schedule=dt.datetime.now() + dt.timedelta(days=7)    
    )
    
    async with channel() as upload:
        await upload.upload_video(video)


asyncio.run(main())
