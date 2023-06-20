#SeleniumSimplified(<img src="https://github.com/raajrajnish/SeleniumSimplified/blob/master/assets/beta.png?raw=true" alt="Logo-SeleniumSimplified beta version" height=25 width=25/>)
<p align="center">
  <img src="https://github.com/raajrajnish/SeleniumSimplified/blob/master/assets/main_logo.png?raw=true" alt="Logo-SeleniumSimplified" height=300 width=300/>
</p>


***A free, open-source web automation library to do anything and everything on the Chrome browser using Python.***

    USE SELENIUM SIMPLIFIED FOR

    1. Browser Automation or Web Scrapping
    2. API automation or Data Scrapping using API
    3. Headless Browser automation

    and many more uses cases



## Description
This library is created keeping those developers in mind who wish to automate their website for a task but do not wish to spend an excessive amount of time learning a new library.We made every effort when creating this toolkit to make web automation as simple and efficient as possible. This library's backend is the Python client for [Selenium](https://www.selenium.dev/). Selenium is the standard library for web automation and is quite powerful.

In order to make things simple and easy to understand for anyone with a background in selenium, we have made an effort to keep the function name as close to the original selenium functions as possible.

## Advantages
This library has below advantages
  1. It is a plug-and-play library built on top of Selenium, you still get the power of Selenium when using it.
  2. It supports the Chrome browser out of the box; internally, everything is taken care of.
  3. It by default highlights the weblement (the target web element on which you wish to conduct some operations) before doing anything.
  4. It use XPATH as a default for the locator strategy.
  5. Saves a tonne of time by preventing us from writing repetitive code because it is simple to setup and use.

## How to install
```pip install selenium-simplified```

## Example
Below code will open chrome browser and navigate to Google home page and do a search for SeleniumSimplified
``` 
from simplified import *

driver = SeleniumSimplified()
driver.open_url(url='https://www.google.com')
driver.type_in_element(xpath="//*[@name='q']",text='selenium')
driver.click_on_element(xpath="//*[@name='btnK']")
```

## Functions Supported
#### Core Functions : 
  1. ***open_url*** - Used for open a url in the chrome browser, takes one param1- as url 
  2. ***type_in_element*** - Used for typing in input box, takes to parameter param1- xpath as locator and param2- as text
  3. ***click_on_element*** - Used for clicking on web-element, takes one param1- as xpath
  4. ***take_screenshot*** - Use when you have to take screenshot, take one param1 as dir (directory name)
  5. ***get_tab_title*** - Use to get the current tab title in the browser, do not take any params
  6. ***close_current_tab*** - Use to close the current tab in focus in the browser,do not take any params
  7. ***close_browser*** - Use for closing the current browser instance including all tabs, do not take any params

adding more functions...

### Example Usage - Core user functions
```commandline
# Step 1 : install the library
# pip install selenium-simplified

# Step 2: import the library
from simplified import SeleniumSimplified

# Step 3 - Open the chrome browser
driver = SeleniumSimplified()

'''
Examples - Showing how to use SeleniumSimplified functions
Please Note - SeleniumSimplified uses XPATH only as its locator strategy
'''

# How to open a specific url
driver.open_url(url='https://www.google.com')

# How to find an element and type some text in it
driver.type_in_element(xpath="//*[@name='q']",text='selenium')

# How to find an element and click on it
driver.click_on_element(xpath="//*[@name='btnK']")

# How to take screenshot and save it inside the screenshot directory
driver.take_screenshot(dir='../screenshot/')

# how to get the current browser tab title
print(driver.get_tab_title())

# How to close the current browser tab
driver.close_current_tab()

# How to close browser
driver.close_browser()
```