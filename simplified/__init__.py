from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .CommonActivities import *
from .AdvannceActivities import *


def open_chrome(universal_wait=10):
    # enabling chrome options
    chrome_options = Options()
    # setting browser not to close after opening chrome
    chrome_options.add_experimental_option("detach", True)
    # removing ribbon from the chrome browser
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # passing the chrome options to chrome instance
    driver = webdriver.Chrome(chrome_options)
    # setting the implicit wait
    driver.implicitly_wait(universal_wait)
    # maximizing the window
    driver.maximize_window()
    # return the driver instance
    return driver


class SeleniumSimplified:
    def __init__(self):
        driver = open_chrome()
        base_functions = CommonActivities(driver=driver)
        self.base_functions = base_functions

    def open_url(self, url):
        self.base_functions.open_url(url=url)

    def get_tab_title(self):
        return self.base_functions.get_title()

    def type_in_element(self, xpath, text):
        self.base_functions.type_in_element(web_element=self.base_functions.element_find(xpath=xpath), text=text)

    def click_on_element(self, xpath):
        self.base_functions.click_on_element(web_element=self.base_functions.element_find(xpath=xpath))

    def web_element(self, xpath):
        return self.base_functions.element_find(xpath=xpath)

    def close_current_tab(self):
        self.base_functions.close_current_tab()

    def close_browser(self):
        self.base_functions.close_browser()

    def get_html_source(self):
        return self.base_functions.get_page_source()

    def take_screenshot(self, dir):
        self.base_functions.click_screenshot(dir=dir)
