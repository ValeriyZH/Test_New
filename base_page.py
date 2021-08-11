from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import unittest
import time

class BasePage:

   

    def assertElementsIsPresentByXpatch(self, xpath_elements):
        try:
            elements = self.find_elements_by_xpath(xpath_elements)
            return [True, len(elements)]
        except NoSuchElementException:
            return [False, 0]

    def assertElementIsPresentByXPath_Click(self, xpath, msg=None):
        try:
            element = self.find_element_by_xpath(xpath).click()
            return True
        except NoSuchElementException:
            return(False)

    def assertElementIsPresentByXPath_Send(self, xpath_input, send_message):
        try:
            element = self.find_element_by_xpath(xpath_input).send_keys(send_message)
            return True
        except NoSuchElementException:
            return(False)

    def element_exists_and_click(self, xpath):
        assert BasePage.assertElementIsPresentByXPath_Click(self, xpath), f'Элемента {xpath} на странице нет'

    def element_exists_and_send(self, xpath_input, send_message):
        assert BasePage.assertElementIsPresentByXPath_Send(self, xpath_input, send_message), f'Элемента {xpath_input} на странице нет'

    def element_exists_count(self, xpath_elements):
        l = BasePage.assertElementsIsPresentByXpatch(self, xpath_elements)
        # для вывода print использовать pytest -s
        print(f'На СТРАНИЦЕ есть всего {l[1]} элемента(ов) {l[0]}')
        assert l[0], f'Элементов {xpath_elements} на странице нет'
        return l[1]

    def scroll_down_link_click(self, xpath_down_link):
      
        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        assert BasePage.assertElementIsPresentByXPath_Click(self, xpath_down_link), f'Элемент {xpath_down_link} внизу страницы не обнаружен'
     
    def drop_down_element_click(self, xpath_drop_down_list, element_text):

        #select = Select(self.find_element_by_xpath(xpath_drop_down))
        #select.select_by_index(index)
        #select.select_by_visible_text("Телефоны").click()
        #select.select_by_value(value)
        
        element = self.find_element_by_xpath(xpath_drop_down_list)
        element.click()
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("text") == element_text:     #print("Value is: %s" % option.get_attribute("value"))
                option.click()
                break

        #BasePage.assertElementIsPresentByXPath_Click(self, xpath_drop_down)
        #element = self.find_element_by_xpath(xpath_drop_down)
        #element.click()
        #driver.execute_script("arguments[0].scrollIntoView();", element)

        #i = 0
        #account_dropdown = self.find_element_by_xpath(xpath_drop_down)
        #child_elements = account_dropdown.find_elements_by_css_selector('*')
        #while i < len(child_elements): # While i is less than the amount of objects in the array
        #    selected_element = child_elements[i] # Grabbing one of the elements from the array depending of what number run this is through the while loop
        #    value = selected_element.get_attribute('text') # Grabbing the attribute innerText from the element
        #    if value == element_text: # Checking to see if the innerText of the current element matches with the one we want
        #        result = selected_element
        #    else:
        #        i += 1
        #result.click()