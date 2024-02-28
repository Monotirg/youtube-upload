# YouTube upload

## Key Features

-   Not using [YouTube APIv3](https://developers.google.com/youtube/)
-   Allowing customization of all YouTube video settings
-   Logging video uploads
-   Supports headless operation
-   Supports asynchronous video uploads

## Installation

```sh
# install youtube-upload
pip install yt-upload
# install chrome browser
playwright install chrome 
```

## Getting started

### Upload video

To upload some video:

``` python
# exmaples/upload_video.py
import asyncio
import yt_upload as yt
import datetime as dt


async def main():
    channel = yt.Channel(
        user_data_dir="User Data",
        profile="Profile 1",
        cookies_path="cookies.json"
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
```

### Upload videos

to upload multiple videos asynchronously:

``` python
# examples/upload_videos.py
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
```

### YouTube video settings

An example YouTube video settings:

``` python
# examples/youtube_video_settings.py.py
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
```

### Logging configure

An example using a logging:

``` python
# examples/logging_configure.py
logging_config = {
    "filename": "yt_log.jsonl",
    "maxBytes": 10000,
    "backupCount": 3,
}

async with channel(enable_logging=True, **logging_config) as upload:
    await upload.upload_video(video)
```

## Requirements

-   [playwright](https://playwright.dev/python/docs/intro)
-   [pymediainfo](https://pypi.org/project/pymediainfo/)
-   [pydantic](https://docs.pydantic.dev/latest/install/)

## License

This project is licensed under the MIT License. See the LICENSE file for
details.
