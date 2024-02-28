'''components on YouTube video details page after uploading video'''

class YTDetailsComponent:
    # daily upload limit reached
    daily_upload_limit_reached_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[1]/ytcp-ve/div[1]"
    

    # input field to video title 
    title_input_xpath = "//ytcp-social-suggestions-textbox[@id='title-textarea']//div[@id='textbox']"
    # input field to video description
    description_input_xpath = "//ytcp-social-suggestions-textbox[@id='description-textarea']//div[@id='textbox']"
    
    # button to select thumbnail image file
    select_thumbnail_button_xpath = "//*[@id='select-button']"
    
    # components to select playlists
    playlist_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[4]/div[3]/div[1]/ytcp-video-metadata-playlists/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    playlist_input_xpath = "//*[@id='search-input']"
    playlist_checkbox_group_xpath = "//*[@id='checkbox-group']/ul"
    playlist_items_xpath = "//html/body/ytcp-playlist-dialog"
    playlist_item_xpath = "//ytcp-ve"
    playlist_item_title_xpath = "//span//span"
    playlist_item_checkbox_xpath = "//*[@id='checkbox']"
    playlist_done_button_xpath = "//*[@id='dialog']/div[2]/ytcp-button[2]/div"

    # components to settings age category 
    made_for_kids_radio_button_xpath = "//tp-yt-paper-radio-button[@name='VIDEO_MADE_FOR_KIDS_MFK']//div[@id='radioContainer']"
    not_made_for_kids_radio_button_xpath = "//tp-yt-paper-radio-button[@name='VIDEO_MADE_FOR_KIDS_NOT_MFK']//div[@id='radioContainer']"
    age_restriction_advanced_button_xpath = "//button[@class='expand-button remove-default-style style-scope ytcp-video-metadata-editor-basics']//tp-yt-iron-icon[2]"
    age_restriction_radio_button_xpath = "//tp-yt-paper-radio-button[@name='VIDEO_AGE_RESTRICTION_SELF']//div[@id='radioContainer']"
    no_age_restriction_radio_button_xpath = "//tp-yt-paper-radio-button[@name='VIDEO_AGE_RESTRICTION_NONE']//div[@id='radioContainer']"
    
    # button to show advanced settings
    show_more_button_xpath = "//ytcp-button[@id='toggle-button']"

    # advanced settings
    # checkboxes
    containts_paid_promotion_checkbox_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[1]/ytcp-checkbox-lit/div/div[1]/div/div"
    allow_automatic_chapters_and_key_checkbox_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[2]/ytcp-form-checkbox/ytcp-checkbox-lit/div/div[1]/div/div"
    allow_automatic_places_checkbox_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[3]/ytcp-checkbox-lit/div/div[1]/div/div"
    allow_automatic_concepts_checkbox_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[4]/ytcp-form-checkbox/ytcp-checkbox-lit/div/div[1]/div/div"
    allow_embedding_checkbox_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[8]/div[4]/ytcp-form-checkbox/ytcp-checkbox-lit/div/div[1]/div/div"
    publish_to_subscriptions_feed_checkbox_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[8]/div[4]/ytcp-checkbox-lit/div/div[1]/div/div"
    show_viewers_like_checkbox_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[5]/ytcp-form-checkbox/ytcp-checkbox-lit/div/div[1]/div/div"

    # radio buttons
    allow_video_audio_remixing_radio_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[9]/ytcp-video-metadata-remix-settings/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]/div[1]"
    allow_only_audio_remixing_radio_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[9]/ytcp-video-metadata-remix-settings/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]"
    
    # input field to video tags
    tags_input_xpath = "//ytcp-form-input-container[@id='tags-container']//input[@id='text-input']"

    # components to select video language
    video_language_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[6]/div[3]/ytcp-form-language-input/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    video_language_items_xpath = "//*[@id='dialog']"
    video_language_item_xpath = "//ytcp-ve"
    video_language_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    video_language_item_by_index_xpath = "//*[@id='text-item-{index}']"

    # components to select caption certification
    caption_certification_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[6]/div[3]/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    caption_certification_items_xpath = "//*[@id='dialog']"
    caption_certification_item_xpath = "//ytcp-ve"
    caption_certification_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    caption_certification_item_by_index_xpath = "//*[@id='text-item-{index}']"

    # components to select recording date
    recording_date_show_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[7]/div[3]/div/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    recording_date_input_xpath = "//html/body/ytcp-date-picker/tp-yt-paper-dialog/div/form/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input"

    # components to select video location
    video_location_input = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[7]/div[3]/ytcp-form-location/ytcp-form-autocomplete/ytcp-dropdown-trigger/div/div[2]/input"
    video_location_items_xpath = "//*[@id='dialog']"
    video_location_item_xpath = "//ytcp-ve"
    video_location_item_title1_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string/span[1]"
    
    # components to select license
    license_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[8]/div[3]/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    license_items_xpath = "//*[@id='dialog']"
    license_item_xpath = "//ytcp-ve"
    license_item_title_xpath = "/tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    license_item_by_index_xpath = "//*[@id='text-item-{index}']"
    
    # components to set category
    category_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[10]/div[3]/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    category_items_xpath = "//*[@id='dialog']"
    category_item_xpath = "//ytcp-ve"
    category_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    category_item_by_index_xpath = "//*[@id='text-item-{index}']"
    
    # components to set game title
    game_title_input_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[10]/ytcp-form-gaming/ytcp-form-autocomplete/ytcp-dropdown-trigger/div/div[2]/input"
    game_title_items_xpath = "//*[@id='dialog']"
    game_title_item_xpath = "//ytcp-ve"
    game_title_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string/span[1]"

    # components to set education type
    education_type_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[10]/ytcp-form-education/ytcp-education-video-metadata/ytcp-form-select[1]/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    education_type_items_xpath = "//*[@id='dialog']"
    education_type_item_xpath = "//ytcp-ve"
    education_type_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    education_type_item_by_index_xpath = "//*[@id='text-item-{index}']"
    
    # input field to education problems
    education_problems_input_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[10]/ytcp-form-education/ytcp-education-video-metadata/ytcp-form-textarea/div/textarea"

    # components to set education academic system
    education_academic_system_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[10]/ytcp-form-education/ytcp-education-video-metadata/ytcp-form-select[2]/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    education_academic_system_items_xpath = "//*[@id='dialog']"
    education_academic_system_item_xpath = "//ytcp-ve"
    education_academic_system_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    education_academic_system_by_index_xpath = "//*[@id='text-item-{index}']"
    
    # components to set education level
    education_level_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[10]/ytcp-form-education/ytcp-education-video-metadata/ytcp-form-select[3]/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    education_level_items_xpath = "//*[@id='dialog']"
    education_level_item_xpath = "//tp-yt-paper-item[@aria-disabled='false']"
    education_level_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    education_level_item_by_index_xpath = "//*[@id='text-item-{index}']"
    
    # components to set education exam
    education_exam_input_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[10]/ytcp-form-education/ytcp-education-video-metadata/ytcp-form-autocomplete/ytcp-dropdown-trigger/div/div[2]/input"
    education_exam_items_xpath = "//*[@id='dialog']"
    education_exam_item_xpath = "//ytcp-ve"
    education_exam_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    education_exam_item_by_index_xpath = "//*[@id='text-item-{index}']"

    # components to select comments and raitings
    comments_and_ratings_on_radio_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[3]/ytcp-comment-moderation-settings/div/tp-yt-paper-radio-button[1]/div[1]"
    comments_and_ratings_off_radio_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[3]/ytcp-comment-moderation-settings/div/tp-yt-paper-radio-button[2]/div[1]"
    comments_moderation_show_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[3]/ytcp-comment-moderation-settings/div/button/tp-yt-iron-icon[2]"
    comments_moderation_none_radio_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[3]/ytcp-comment-moderation-settings/div/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]/div[1]"
    comments_moderation_basic_radio_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[3]/ytcp-comment-moderation-settings/div/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]"
    comments_moderation_strict_radio_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[3]/ytcp-comment-moderation-settings/div/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]"
    comments_moderation_hold_all_radio_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[3]/ytcp-comment-moderation-settings/div/tp-yt-paper-radio-group/tp-yt-paper-radio-button[4]/div[1]"

    # components to set sort by
    sort_by_show_paper_list_button_xpath = "//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[11]/div[4]/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/tp-yt-iron-icon"
    sort_by_items_xpath = "//*[@id='dialog']"
    sort_by_item_xpath = "//ytcp-ve"
    sort_by_item_title_xpath = "//tp-yt-paper-item-body/div/div/div/yt-formatted-string"
    sort_by_item_by_index_xpath = '//*[@id="text-item-{index}"]'

    # button to move next section
    next_button_xpath = "//ytcp-button[@id='next-button']"

    # target ytcp-text-menu by index
    ytcp_text_menu_by_index = "//html/body/ytcp-text-menu[{index}]"

    # last ytcp-text-menu
    last_ytcp_text_menu = "//html/body/ytcp-text-menu[last()]"

    # ytcp-text-menu target element
    target_element_ytcp_text_menu = "//*[@id='text-item-2']"
