==================================
YouTube upload videos  
==================================


Key Features
============

- `APIv3 <https://developers.google.com/youtube/>`_  is not used
- All YouTube video settings are available
- Logging uploading videos 
- Supports Headless operation
- Supports asynchronous videos upload


Getting started
===============

Upload video
------------

To upload some video:

.. code-block:: python

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


Upload videos 
-------------

to upload multiple videos asynchronously:

.. code-block:: python

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


YouTube video settings
----------------------

An example YouTube video settings:

.. code-block:: python

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

Logging configure
-----------------

An example using a logging:

.. code-block:: python

    # examples/logging_configure.py
    logging_config = {
        "filename": "yt_log.jsonl",
        "maxBytes": 10000,
        "backupCount": 3,
    }

    async with channel(enable_logging=True, **logging_config) as upload:
        await upload.upload_video(video)


Requirements
============

- playwright_
- pymediainfo_
- pydantic_

.. _playwright: https://playwright.dev/python/docs/intro
.. _pymediainfo: https://pypi.org/project/pymediainfo/
.. _pydantic: https://docs.pydantic.dev/latest/install/

License
=======

Distributed under the MIT License.
