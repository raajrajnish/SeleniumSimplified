# SeleniumSimplified 
<p align="center">
  <img src="https://github.com/raajrajnish/SeleniumSimplified/blob/master/assets/Se.png?raw=true" alt="Logo-SeleniumSimplified" height=300 width=300/>
</p>
A free, open-source web automation library for the Chrome browser using Selenium Python.

### Description
This library is created keeping those developers in mind who wish to automate their website for a task but do not wish to spend an excessive amount of time learning a new library.We made every effort when creating this toolkit to make web automation as simple and efficient as possible. This library's backend is the Python client for [Selenium](https://www.selenium.dev/). Selenium is the standard library for web automation and is quite powerful.

In order to make things simple and easy to understand for anyone with a background in selenium, we have made an effort to keep the function name as close to the original selenium functions as possible.

### Advantages
This library has below advantages
  1. It is a plug-and-play library built on top of Selenium, you still get the power of Selenium when using it.
  2. It supports the Chrome browser out of the box; internally, everything is taken care of.
  3. It by default highlights the weblement (the target web element on which you wish to conduct some operations) before doing anything.
  4. It use XPATH as a default for the locator strategy.
  5. Saves a tonne of time by preventing us from writing repetitive code because it is simple to setup and use.

### How to install
```pip install selenium-simplified```

### Example
Below code will open chrome browser and navigate to Google home page and do a search for SeleniumSimplified
``` 
from simplified import *

driver = SeleniumSimplified()
driver.open_url(url='https://www.google.com')
driver.type_in_element(xpath="//*[@name='q']",text='selenium')
driver.click_on_element(xpath="//*[@name='btnK']")
```

### Functions Supported
  1. ***open_url*** - Used for open a url in the chrome browser, takes one param1- as url 
  2. ***type_in_element*** - Used for typing in input box, takes to parameter param1- xpath as locator and param2- as text
  3. ***click_on_element*** - Used for clicking on webelement, takes one param1- as xpath

adding more functions...
