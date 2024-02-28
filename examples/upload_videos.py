import asyncio
import yt_upload as yt


async def main():
    channel = yt.Channel(
        user_data_dir="User Data",
        profile="Profile 1",
        cookies_path="cookies.json"
    )
    video1 = yt.Video(
        video_path="video1.mp4",
        title="Funny video 1",
        made_for_kids=False,
        category=yt.category.PETS_ANIMALS,
        visibility=yt.visibility.PUBLIC,
    )
    video2 = yt.Video(
        video_path="video2.mp4",
        title="Funny video 2",
        made_for_kids=False,
        category=yt.category.PETS_ANIMALS,
        visibility=yt.visibility.PUBLIC,
    )
    
    async with channel() as upload:
        await upload.upload_videos([video1, video2])


asyncio.run(main())
