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


Logging configure
-----------------

An example using a logging:

.. code-block:: python

    # examples/logging_configure.py
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
        
        logging_config = {
            "filename": "yt_log.jsonl",
            "maxBytes": 10000,
            "backupCount": 3,
        }


        async with channel(**logging_config) as upload:
            await upload.upload_video(video)


    asyncio.run(main())


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

This project is licensed under the MIT License. See the LICENSE file for details.
