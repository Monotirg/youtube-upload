
import re
import asyncio

from datetime import datetime
from playwright.async_api import Page

from ._YTPage import YTPage
from .times import TimeOut, TimeSleep
from ..constants.visibilities import PUBLIC, UNLISTED
from ..components._YTVisibilityComponent import YTVisibilityComponent
from ..utils import datetime_to_yt_date


KB_ENTER = "Enter"


class YTVisibilityPage(YTPage):
    component = YTVisibilityComponent
    time_out = TimeOut
    time_sleep = TimeSleep

    match_status = re.compile(r"Uploading.*%")

    
    def __init__(self, page: Page) -> None:
        self.page = page

    async def press_show_schedule(self):
        await self.page.locator(
            YTVisibilityPage.component.schedule_show_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def input_schedule(self, schedule: datetime):
        date, time = datetime_to_yt_date(schedule)

        await self.press_show_schedule()
        await self.page.locator(
            YTVisibilityPage.component.schedule_time_input_xpath
        ).fill(
            time,
            timeout=self.time_out.fill
        )
        await self.page.locator(
            YTVisibilityPage.component.schedule_date_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTVisibilityPage.component.schedule_date_input_xpath
        ).fill(
            date, 
            timeout=self.time_out.fill)
        await self.page.keyboard.press(KB_ENTER)
        
    async def input_visibility(self, visibility: str):
        if visibility == PUBLIC:
            await self.press_public()
        elif visibility == UNLISTED:
            await self.press_unlisted()
        else:
            await self.press_private()
        
    async def press_private(self):
        await self.page.locator(
            YTVisibilityPage.component.private_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_unlisted(self):
        await self.page.locator(
            YTVisibilityPage.component.unlisted_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_public(self):
        await self.page.locator(
            YTVisibilityPage.component.public_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_save(self):
        await self.page.locator(
            YTVisibilityPage.component.save_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.wait_for_timeout(
            self.time_sleep.save_button
        )
     
    async def press_close(self):
        await self.page.locator(
            YTVisibilityPage.component.close_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def verify_upload_video(self):
        while True:
            upload_status = await self.page.locator(
            YTVisibilityPage.component.upload_video_progress_bar_xpath
            ).text_content()
            status = YTVisibilityPage.match_status.findall(upload_status)
            
            if not status:
                break

            await self.page.wait_for_timeout(1)
