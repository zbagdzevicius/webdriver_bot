import pytest
from webdriver_bot import SeleniumBot
from time import sleep


class TestSelenium():
    def setup_class(self):
        self.bot = SeleniumBot()

    def test_bot(self):
        self.bot.go_to_page('https://www.cheetos.lv/index/galerii/images/librariesprovider2/osalejad/gailene88f34b0e1eb34f5786f4e0206ee9ab2f?itemIndex=3')
        self.bot.driver.save_screenshot('test_bot.png')
    
    def test_captcha(self):
        all_iframes =self.bot.driver.find_elements_by_css_selector("iframe")
        print(all_iframes)
        captcha_frame = self.bot.get_element_by_css_selector("iframe[sandbox='allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox']")
        self.bot.driver.switch_to.frame(captcha_frame)
        sleep(10)
        im_not_robot_button = self.bot.get_element_by_css_selector(".rc-anchor-checkbox-holder")
        self.bot.post_click_or_submit(im_not_robot_button)
        challenge_frame = self.bot.get_element_by_css_selector("iframe[title='recaptcha challenge']")
        self.bot.driver.switch_to.default_content()
        self.bot.driver.switch_to.frame(challenge_frame)
        audio_button = self.bot.get_element_by_css_selector("buton#recaptcha-audio-button")
        self.bot.post_click_or_submit(audio_button)
        self.bot.driver.save_screenshot('after_click.png')