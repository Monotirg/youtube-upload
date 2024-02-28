import asyncio

from playwright.async_api import Page

from ._YTPage import YTPage
from .times import TimeOut, TimeSleep
from ..components import YTStudioComponent


class YTStudioPage(YTPage):
    component = YTStudioComponent
    time_out = TimeOut
    time_sleep = TimeSleep

    youtube_url = "https://www.youtube.com"
    studio_url = "https://studio.youtube.com"
    

    def __init__(self, page: Page) -> None:
        self.page = page

    async def load_page(self):  
        await self.page.goto(
            YTStudioPage.studio_url, 
            timeout=self.time_out.GLOBAL,
            wait_until='domcontentloaded'
        )
        await self.page.wait_for_selector(
            YTStudioPage.component.create_button_xpath, 
            timeout=self.time_out.GLOBAL
        )      
        
    async def input_video(self, filepath: str):
        await self.page.locator(
            YTStudioPage.component.create_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTStudioPage.component.upload_videos_button_xpath
        ).click(
            timeout=self.time_out.click)

        async with self.page.expect_file_chooser(
            timeout=self.time_out.select_files
        ) as fc_info:
            await self.page.locator(
                YTStudioPage.component.select_file_button_xpath
            ).click(
                timeout=self.time_out.click
            )

        file_chooser = await fc_info.value
        await file_chooser.set_files(
            filepath, 
            timeout=self.time_out.upload_files
        )
        await self.page.wait_for_timeout(
            self.time_sleep.upload_files
        )

    async def get_language(self):
        await self.page.goto(
            YTStudioPage.youtube_url,
            wait_until='domcontentloaded'
        )

        language = await self.page.locator(
            YTStudioComponent.html
        ).get_attribute(
            "lang"
        )

        return language

    async def change_language_to_eng(self): 
        
        await self.page.locator(
            YTStudioPage.component.account_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTStudioPage.component.language_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTStudioPage.component.language_paper_list_items_xpath
        ).get_by_text(
            YTStudioPage.component.english_item_text
        ).click(
            timeout=self.time_out.click
        )
