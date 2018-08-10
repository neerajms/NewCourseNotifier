import urllib
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from studip_credentials import studip


def check_for_changes():
    # URL of the StudIP Login page of Uni Passau
    login_url = "https://studip.uni-passau.de/studip/index.php"

    # Initialize browser, find username and password elements, pass their values
    browser = webdriver.Firefox()  # Instance of firefox webdriver is created
    browser.get(login_url)  # Open the login_url using firefox
    browser.find_element_by_partial_link_text("for students and employees").click()

    # On the login page
    user_name = browser.find_element_by_id("username")  # Get the username element
    password = browser.find_element_by_id("password")  # Get the password element
    button = browser.find_element_by_name("_eventId_proceed")  # Get button
    user_name.clear()  # Clear username element
    password.clear()  # Clear password element
    user_name.send_keys(studip.get("user_name"))  # Pass the value of username
    password.send_keys(studip.get("password"))  # Pass the value of password
    button.click()  # Click log in button

    # On the user start page
    course_search_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[5]/ul/li[6]/a")))  # Locate the element to search for courses
    course_search_element.click()  # Click the search button to go to search page

    assert "No results found." not in browser.page_source


check_for_changes()
