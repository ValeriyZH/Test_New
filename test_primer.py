from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage as Base
import time



url = 'https://avito.ru'

xpath = '//a[contains(text(),"Авто")]'
xpath_input = '//input[@id="search"]'
xpath_button = '//button[@data-marker="search-form/submit-button"]'
xpath_down_link = '//a[@href="https://vk.com/avito"]'
xpath_drop_down_list = '//div/select[@id="category"]'
xpath_drop_down_element = '//div/select/option[contains(text(),"Телефоны")]'

element_text = 'Телефоны'
message_input = 'Toyota Sequoia, 2008'

xpath_elements = '//li[@class="rubricator-list-item-item-tP77G rubricator-list-item-item-expandable-U9dac rubricator-list-item-item_closed-10ZHG"]'
  
def __init__(self, browser):
    self.browser = browser


def test_primer(browser):
    browser.set_window_size (1920, 1080)
    browser.get(url)
    Base.element_exists_and_click(browser, xpath_drop_down_list)
    Base.drop_down_element_click(browser, xpath_drop_down_list, element_text)
    time.sleep(5)
    Base.element_exists_and_click(browser, xpath)
    Base.element_exists_and_send(browser, xpath_input, message_input)
    Base.element_exists_and_click(browser, xpath_button)
    count_elements = Base.element_exists_count(browser, xpath_elements)
    Base.scroll_down_link_click(browser, xpath_down_link)
    time.sleep(5)
    