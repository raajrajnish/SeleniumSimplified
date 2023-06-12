from UserActions import *

driver = SeleniumSimplified()
driver.open_url(url='http://www.google.com')
driver.type_in_element(xpath="//*[@name='q']",text='selenium simplified')
driver.click_on_element(xpath="//*[@name='btnK']")