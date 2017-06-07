from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('http://www.facebook.com')
elem = browser.find_element_by_name('email')  # Find the search box
elem.send_keys('sathya' + Keys.RETURN)
elem1 = browser.find_element_by_name('pass')  # Find the search box
elem1.send_keys('abc' + Keys.RETURN)
