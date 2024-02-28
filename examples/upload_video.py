import asyncio
import yt_upload as yt
import datetime as dt


async def main():
    channel = yt.Channel(
        user_data_dir="User Data",
        profile="Profile 1",
        cookies_path="cookies/cookies.json"
    )
    video = yt.Video(
        video_path="video.mp4",
        title="Funny video",
        made_for_kids=False,
        category=yt.category.PETS_ANIMALS,
        visibility=yt.visibility.PUBLIC,
        tags=["animals", "cats",  "funny"],
        schedule=dt.datetime.now() + dt.timedelta(days=1)
    )
    
    async with channel() as upload:
        await upload.upload_video(video)


asyncio.run(main())
