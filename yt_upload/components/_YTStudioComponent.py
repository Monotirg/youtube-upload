'''components on YouTube studio home page'''

class YTStudioComponent:
    # html-doc
    html = "//html"
    # show account settings
    account_button_xpath = "//*[@id='avatar-btn']"
    language_show_paper_list_button_xpath = "//html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[3]/div[2]/ytd-compact-link-renderer[2]/a/tp-yt-paper-item"
    language_paper_list_items_xpath = "//html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]"
    
    # english language text 
    english_item_text = "English (US)"
    
    # create button
    create_button_xpath = "//*[@id='create-icon']"
    
    # upload video
    upload_videos_button_xpath = "//*[@id='text-item-0']/ytcp-ve"
    
    # select video file
    select_file_button_xpath = "//ytcp-button[@id='select-files-button']"
