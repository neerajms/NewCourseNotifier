import urllib
import re
from selenium import webdriver
from studip_credentials import studip


def check_for_changes():
    # URL of the StudIP Login page of Uni Passau
    login_url = "https://studip.uni-passau.de/studip/index.php"

    # Initialize browser, find username and password elements, pass their values
    browser = webdriver.Firefox()  # Instance of firefox webdriver is created
    browser.get(login_url)  # Open the login_url using firefox
    browser.find_element_by_partial_link_text("for students and employees").click()
    user_name = browser.find_element_by_id("username")  # Get the username element
    password = browser.find_element_by_id("password")  # Get the password element
    button = browser.find_element_by_name("_eventId_proceed")  # Get button
    user_name.clear()  # Clear username element
    password.clear()  # Clear password element
    user_name.send_keys(studip.get("user_name"))  # Pass the value of username
    password.send_keys(studip.get("password"))  # Pass the value of password
    button.click()
    assert "No results found." not in browser.page_source


check_for_changes()
