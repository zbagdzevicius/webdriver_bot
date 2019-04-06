import pytest
from webdriver_bot import SeleniumBot

def test_bot():
    bot = SeleniumBot()
    bot.go_to_page('https://google.com')