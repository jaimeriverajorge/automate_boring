# This program makes use of the Selenium module to perform the following tasks:
# Open up a Firefox browser
# navigate the browser to a webpage
# click on a link within the webpage

from selenium import webdriver
# this import statement is needed to find an element by CSS_SELECTOR
from selenium.webdriver.common.by import By

#opens up a new Firefox window
browser = webdriver.Firefox()
#navigates the Firefox window to the url entered
browser.get('https://automatetheboringstuff.com')

#finds the "Introduction" link on the browser
elem = browser.find_element(By.CSS_SELECTOR, ".main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(1) > a:nth-child(1)")
#goes to the link that was found
elem.click()

# can be used to go back, forward, and refresh
browser.back()
browser.forward()
browser.refresh()

# quits the browser
browser.quit()
