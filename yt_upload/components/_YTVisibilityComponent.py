'''components on YouTube visibility page'''

class YTVisibilityComponent:
    # noqa
    language_xpath = "//html"
    
    private_radio_button_xpath = "//tp-yt-paper-radio-button[@id='private-radio-button']//div[@id='radioContainer']"
    unlisted_radio_button_xpath = "//tp-yt-paper-radio-button[@name='UNLISTED']//div[@id='radioContainer']"
    public_radio_button_xpath = "//tp-yt-paper-radio-button[@name='PUBLIC']//div[@id='radioContainer']"
    
    schedule_show_button_xpath = "//div[@id='second-container']//ytcp-icon-button"
    schedule_date_button_xpath = "//ytcp-text-dropdown-trigger[@id='datepicker-trigger']//tp-yt-iron-icon"
    schedule_date_input_xpath = "//ytcp-date-picker//tp-yt-paper-dialog//form//input"
    schedule_time_input_xpath = "//form//tp-yt-paper-input//input"
    
    upload_video_progress_bar_xpath = "//*[@id='dialog']/div/ytcp-animatable[2]/div/div[1]/ytcp-video-upload-progress/span"
    
    save_button_xpath = "//ytcp-button[@id='done-button']"
    close_button_xpath = "//*[@id='close-button']/div"
