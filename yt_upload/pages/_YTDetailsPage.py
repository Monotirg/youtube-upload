import asyncio
import warnings
import logging

from playwright.async_api import Page
from datetime import datetime

from ..constants.indexes import *
from ._YTPage import YTPage
from .times import TimeOut, TimeSleep
from ..exceptions import YTWarning, YTError
from ..components import YTDetailsComponent
from ..constants.comment_moderations import BASIC, STRICT, HOLD_ALL
from ..utils import datetime_to_yt_date


KB_ENTER = "Enter"


logger = logging.getLogger("yt_logger")

class YTDetailsPage(YTPage):
    component = YTDetailsComponent
    time_out = TimeOut
    time_sleep = TimeSleep


    def __init__(self, page: Page):
        self.page = page
        self.ytcp_text_menu_cnt = 1

    async def had_daily_upload_limit_reached(self):
        check_limit = await self.page.query_selector(
            YTDetailsPage.component.daily_upload_limit_reached_xpath
        )


        if check_limit is not None:
            check_limit = await self.page.locator(
                YTDetailsPage.component.daily_upload_limit_reached_xpath
            ).text_content()
            print(check_limit)
            raise YTError(f"Daily upload reached {check_limit}")
        
        return None

    def had_daily_upload_limit_reached_decorator(func):
        async def wrapper(self, *args, **kwargs):
            await self.had_daily_upload_limit_reached()
            await func(self, *args, **kwargs)

        return wrapper

    async def _extract_paper_list_items(
        self,
        list_xpath: str,
        item_xpath: str,
        attr_xpath: str
    ):

        await self.page.wait_for_selector(
            YTDetailsPage.component.ytcp_text_menu_by_index.format(
                index=self.ytcp_text_menu_cnt
            ), 
            state='attached'
        )
        
        self.ytcp_text_menu_cnt += 1

        items = await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            list_xpath
        ).locator(
            item_xpath
        ).all()
        
        data = []
        
        for item in items:
            title = await item.locator(attr_xpath).all_inner_texts()
        
            if title:
                data.append(title[0].strip())

        return data
        
    @had_daily_upload_limit_reached_decorator
    async def input_title(self, title: str):
        await self.page.locator(
            YTDetailsPage.component.title_input_xpath
        ).fill(
            title, 
            timeout=self.time_out.fill
        )
    
    async def input_description(self, description: str):
        await self.page.locator(
            YTDetailsPage.component.description_input_xpath
        ).fill(
            description, 
            timeout=self.time_out.fill
        )

    async def input_thumbnail(self, filepath: str):
        thumbnail_button = await self.page.query_selector(
            YTDetailsPage.component.select_thumbnail_button_xpath
        )

        if thumbnail_button is None:
            msg = (f"Cannot choose a thumbnail for Shorts. "
                   f"Thumbnail will be skipped")
            warnings.warn(msg, YTWarning)
            return None

        async with self.page.expect_file_chooser(
            timeout=self.time_out.select_files
        ) as fc_info:
            await self.page.locator(
                YTDetailsPage.component.select_thumbnail_button_xpath
            ).click(
                timeout=self.time_out.click
            )

        file_chooser = await fc_info.value
        await file_chooser.set_files(filepath, timeout=self.time_out.upload_files)
        await self.page.wait_for_timeout(self.time_sleep.upload_files)

    async def _extract_playlists(self):    
        await self.page.wait_for_selector(
            YTDetailsPage.component.playlist_items_xpath,
            state='attached'
        )

        items = await self.page.locator(
            YTDetailsPage.component.playlist_items_xpath
        ).locator(
            YTDetailsPage.component.playlist_item_xpath
        ).all()

        data = []

        for item in items:
            title = await item.locator(
                YTDetailsPage.component.playlist_item_title_xpath
            ).all_inner_texts()
            data.append(title[0].strip())
        
        return data

    async def input_playlist(self, playlists: list[str]):
        await self.page.locator(
            YTDetailsPage.component.playlist_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.wait_for_selector(
            YTDetailsPage.component.playlist_checkbox_group_xpath
        )
        
        accessible_playlists = await self._extract_playlists()
        skipped_playlists = []

        for playlist in playlists:
            if playlist not in accessible_playlists:
                skipped_playlists.append(playlist)
                continue

            await self.page.locator(
                YTDetailsPage.component.playlist_input_xpath
            ).fill(
                playlist, 
                timeout=self.time_out.fill
            )
            await self.page.get_by_role(
                'checkbox',
                name=playlist
            ).click(
                timeout=self.time_out.click
            )
            
        await self.page.locator(
            self.component.playlist_done_button_xpath
        ).click(
            timeout=self.time_out.click
        )

        if skipped_playlists:
            msg = f"Skipped playlists '{skipped_playlists}'."
            warnings.warn(msg, YTWarning)

    @had_daily_upload_limit_reached_decorator
    async def input_made_for_kids(self, made_for_kids: bool):
        if made_for_kids:
            await self.press_made_for_kids()
        else:
            await self.press_not_made_for_kids()

    async def press_made_for_kids(self):
        await self.page.locator(
            YTDetailsPage.component.made_for_kids_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_not_made_for_kids(self):
        await self.page.locator(
            YTDetailsPage.component.not_made_for_kids_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_age_restriction_advanced(self):
        await self.page.locator(
            YTDetailsPage.component.age_restriction_advanced_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def input_age_restriction(self, age_restriction: str):
        await self.press_age_restriction_advanced()

        if age_restriction:
            await self.press_age_restriction()
        else:
            await self.press_no_age_restriction()

    async def press_age_restriction(self):
        await self.page.locator(
            YTDetailsPage.component.age_restriction_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_no_age_restriction(self):
        await self.page.locator(
            YTDetailsPage.component.no_age_restriction_radio_button_xpath
        ).click(
            timeout=self.time_out.click)

    @had_daily_upload_limit_reached_decorator
    async def press_show_more(self):
        await self.page.locator(
            YTDetailsPage.component.show_more_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def set_contains_paid_promotion(self, is_checked: bool):
        await self.page.locator(
            YTDetailsPage.component.containts_paid_promotion_checkbox_xpath
        ).set_checked(
            is_checked, 
            timeout=self.time_out.click
        )

    async def set_allow_automatic_chapters_and_key(self, is_checked: bool):
        await self.page.locator(
            YTDetailsPage.component.allow_automatic_chapters_and_key_checkbox_xpath
        ).set_checked(
            is_checked, 
            timeout=self.time_out.click
        )

    async def set_allow_automatic_places(self, is_checked: bool):
        await self.page.locator(
            YTDetailsPage.component.allow_automatic_places_checkbox_xpath
        ).set_checked(
            is_checked, 
            timeout=self.time_out.click
        )

    async def set_allow_automatic_concepts(self, is_checked: bool):
        await self.page.locator(
            YTDetailsPage.component.allow_automatic_concepts_checkbox_xpath
        ).set_checked(
            is_checked, 
            timeout=self.time_out.click
        )

    async def set_allow_embedding(self, is_checked: bool):
        await self.page.locator(
            YTDetailsPage.component.allow_embedding_checkbox_xpath
        ).set_checked(
            is_checked, 
            timeout=self.time_out.click
        )
    
    async def set_publish_to_subscriptions_feed(self, is_checked: bool):
        await self.page.locator(
            YTDetailsPage.component.publish_to_subscriptions_feed_checkbox_xpath
        ).set_checked(
            is_checked, 
            timeout=self.time_out.click
        )
    
    async def set_show_viewers_like(self, is_checked: bool):
        await self.page.locator(
            YTDetailsPage.component.show_viewers_like_checkbox_xpath
        ).set_checked(
            is_checked,
            timeout=self.time_out.click
        )

    async def input_remixing_only_audio(self, remixing: bool):
        if remixing:
            await self.press_allow_only_audio_remixing()
        else:
            await self.press_allow_video_audio_remixing()

    async def press_allow_video_audio_remixing(self):
        await self.page.locator(
            YTDetailsPage.component.allow_video_audio_remixing_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_allow_only_audio_remixing(self):
        await self.page.locator(
            YTDetailsPage.component.allow_only_audio_remixing_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def input_tags(self, tags: list[str]):
        await self.page.locator(
            YTDetailsPage.component.tags_input_xpath
        ).fill(
            ",".join(tags), 
            timeout=self.time_out.fill
        )

    async def input_video_language(self, language: str):
        self.ytcp_text_menu_cnt += 1
        language_index = YT_LANGUAGE_TO_INDEX[language]

        await self.page.locator(
            YTDetailsPage.component.video_language_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )

        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.video_language_item_by_index_xpath.format(
                index=language_index
            )
        ).click(
            timeout=self.time_out.click
        )

    async def input_caption_certification(self, caption_certification: str):
        self.ytcp_text_menu_cnt += 1
        caption_certification_index = YT_CAPTION_CERTIFICATION_TO_INDEX[caption_certification]

        await self.page.locator(
            YTDetailsPage.component.caption_certification_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.caption_certification_item_by_index_xpath.format(
                index=caption_certification_index
            )
        ).click(
            timeout=self.time_out.click
        )

    async def input_recording_date(self, date: datetime):
        date = datetime_to_yt_date(date)

        await self.page.locator(
            YTDetailsPage.component.recording_date_show_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTDetailsPage.component.recording_date_input_xpath
        ).fill(
            date,
            timeout=self.time_out.fill
        )
        await self.page.keyboard.press(KB_ENTER)
        
    async def input_video_location(self, video_location: datetime):
        await self.page.locator(
            YTDetailsPage.component.video_location_input
        ).fill(
            video_location,
            timeout=self.time_out.fill
        )

        video_locations = await self._extract_paper_list_items(
            YTDetailsPage.component.video_location_items_xpath,
            YTDetailsPage.component.video_location_item_xpath,
            YTDetailsPage.component.video_language_item_title_xpath
        )
        
        if len(video_locations) <= 1 or video_location not in video_locations[1]:
            msg = (f"Video location '{video_location}' is not found. "
                   f"It will be skipped")
            warnings.warn(msg, YTWarning)
            return None
        
        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.target_element_ytcp_text_menu
        ).click(
            timeout=self.time_out.click
        )

    async def input_license(self, license: str):
        self.ytcp_text_menu_cnt += 1
        caption_certification_index = YT_LICENSE_TO_INDEX[license]

        await self.page.locator(
            YTDetailsPage.component.license_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.license_item_by_index_xpath.format(
                index=caption_certification_index
            )
        ).click(
            timeout=self.time_out.click
        )
    
    @had_daily_upload_limit_reached_decorator
    async def input_category(self, category: str):
        self.ytcp_text_menu_cnt += 1
        category_index = YT_CATEGORIES_INDEX[category]

        await self.page.locator(
            YTDetailsPage.component.category_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.category_item_by_index_xpath.format(
                index=category_index
            )
        ).click(
            timeout=self.time_out.click
        )

    async def input_game_title(self, game_title: str):
        await self.page.locator(
            YTDetailsPage.component.game_title_input_xpath
        ).fill(
            game_title,
            timeout=self.time_out.fill
        )
        
        game_titles = await self._extract_paper_list_items(
            YTDetailsPage.component.game_title_items_xpath,
            YTDetailsPage.component.game_title_item_xpath,
            YTDetailsPage.component.game_title_item_title_xpath
        )

        if game_title not in game_titles:
            msg = (f"'{game_title}' game title is not found. "
                   f"It will be skipped")
            warnings.warn(msg, YTWarning)
            return None

        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.target_element_ytcp_text_menu
        ).click(
            timeout=self.time_out.click
        )
                
    async def input_education_type(self, education_type: str):
        self.ytcp_text_menu_cnt += 1
        education_type_index = YT_EDUCATION_TYPES_TO_INDEX[education_type]

        await self.page.locator(
            YTDetailsPage.component.education_type_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.education_type_item_by_index_xpath.format(
                index=education_type_index
            )
        ).click(
            timeout=self.time_out.click
        )

    async def input_education_problems(self, education_problems: list[str]):
        education_problems_text = "\n".join([
            "{0:02}:{1:02} {2}".format(
                *divmod(t.seconds, 60), 
                problem
            ) 
            for t, problem in education_problems
        ])
        
        await self.page.locator(
            YTDetailsPage.component.education_problems_input_xpath
        ).fill(
            education_problems_text,
            timeout=self.time_out.fill
        )

    async def input_education_academic_system(self, education_academic_system: str):
        self.ytcp_text_menu_cnt += 1
        education_academic_system_index = YT_EDUCATION_ACADEMIC_SYSTEM_TO_INDEX[education_academic_system]

        await self.page.locator(
            YTDetailsPage.component.education_academic_system_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.education_academic_system_by_index_xpath.format(
                index=education_academic_system_index
            )
        ).click(
            timeout=self.time_out.click
        )

    async def input_education_level(self, education_level: str):
        await self.page.locator(
            YTDetailsPage.component.education_level_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        
        accessible_education_levels = await self._extract_paper_list_items(
            YTDetailsPage.component.education_level_items_xpath,
            YTDetailsPage.component.education_level_item_xpath,
            YTDetailsPage.component.education_level_item_title_xpath
        )
        
        if education_level not in accessible_education_levels:
            msg = (f"Education level '{education_level}' is not found in {accessible_education_levels}. "
                   f"It will be skipped")
            warnings.warn(msg, YTWarning)
            return None

        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).get_by_text(
            education_level
        ).click(
            timeout=self.time_out.click
        )

    async def input_education_exam(self, education_exam: str):
        await self.page.locator(
            YTDetailsPage.component.education_exam_input_xpath
        ).fill(
            education_exam, 
            timeout=self.time_out.fill
        )

        accessible_education_exams = await self._extract_paper_list_items(
            YTDetailsPage.component.education_exam_items_xpath,
            YTDetailsPage.component.education_exam_item_xpath,
            YTDetailsPage.component.education_exam_item_title_xpath
        )

        if education_exam not in accessible_education_exams:
            msg = (f"'{education_exam}' education exam is not found. "
                   f"It will be skipped")
            warnings.warn(msg, YTWarning)
            return None
        
        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.target_element_ytcp_text_menu
        ).click(
            timeout=self.time_out.click
        )

    async def input_comment_and_ratings(self, comment_and_ratings):
        if comment_and_ratings:
            await self.press_comments_and_ratings_on()
        else:
            await self.press_comments_and_ratings_off()

    async def press_comments_and_ratings_on(self):
        await self.page.locator(
            YTDetailsPage.component.comments_and_ratings_on_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_comments_and_ratings_off(self):
        await self.page.locator(
            YTDetailsPage.component.comments_and_ratings_off_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )
    
    async def input_comments_moderation(self, comment_moderation: str):
        await self.press_comments_moderation_show()

        if comment_moderation == BASIC:
            await self.press_comments_moderation_basic()
        elif comment_moderation == HOLD_ALL:
            await self.press_comments_moderation_hold_all()
        elif comment_moderation == STRICT:
            await self.press_comments_moderation_strict()
        else:
            await self.press_comments_moderation_none()
        
    async def press_comments_moderation_show(self):
        await self.page.locator(
            YTDetailsPage.component.comments_moderation_show_button_xpath
        ).click(
            timeout=self.time_out.click
        )
    
    async def press_comments_moderation_none(self):
        await self.page.locator(
            YTDetailsPage.component.comments_moderation_none_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )
    
    async def press_comments_moderation_basic(self):
        await self.page.locator(
            YTDetailsPage.component.comments_moderation_basic_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )
    
    async def press_comments_moderation_strict(self):
        await self.page.locator(
            YTDetailsPage.component.comments_moderation_strict_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def press_comments_moderation_hold_all(self):
        await self.page.locator(
            YTDetailsPage.component.comments_moderation_hold_all_radio_button_xpath
        ).click(
            timeout=self.time_out.click
        )

    async def input_sort_by(self, sort_by: str):
        self.ytcp_text_menu_cnt += 1
        sort_by_index = YT_SORT_BY_TO_INDEX[sort_by]

        await self.page.locator(
            YTDetailsPage.component.sort_by_show_paper_list_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.locator(
            YTDetailsPage.component.last_ytcp_text_menu
        ).locator(
            YTDetailsPage.component.sort_by_item_by_index_xpath.format(
                index=sort_by_index
            )
        ).click(
            timeout=self.time_out.click
        )

    @had_daily_upload_limit_reached_decorator
    async def press_next(self):
        await self.page.locator(
            YTDetailsPage.component.next_button_xpath
        ).click(
            timeout=self.time_out.click
        )
        await self.page.wait_for_timeout(self.time_sleep.next_button)
