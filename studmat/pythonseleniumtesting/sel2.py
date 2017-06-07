from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('http://www.facebook.com')
browser.find_element_by_link_text('Sign Up').click()
