from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os.path

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
        expected_conditions.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[5]/ul/li[6]/a")))  # Locate the element to search for courses
    course_search_element.click()  # Click the search button to go to search page

    # On the search page
    search_course_directory_element = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH,
             "/html/body/div[2]/div[6]/div[2]/div[2]/table[2]/tbody/tr/td/div/font/table/tbody/tr/td[2]")))  # Locate the search course directory element
    search_course_directory_element.click()  # Click on search course directory element
    # Continued on the search page
    fakultaet_informatik_mathematik_link = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH,
             "/html/body/div[2]/div[6]/div[2]/div[2]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/ul/li[5]/a")))  # Locate the faculty of informatik and mathematik element
    fakultaet_informatik_mathematik_link.click()  # Click on faculty of informatik and mathematik element
    # Continued on the search page
    master_informatik_link = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH,
             "/html/body/div[2]/div[6]/div[2]/div[2]/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/ul/li[6]/a")))  # Locate the master informatik link
    master_informatik_link.click()  # Click on master informatik link
    # Continued on the search page
    semester_list_item = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH,
             "/html/body/div[2]/div[6]/div[2]/div[2]/form/fieldset/label[4]/div/select/option[6]")))  # Locate WS18/19 list item
    semester_list_item.click()  # Click on list item WS18/19
    # Continued on the search page
    search_button = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH,
             "/html/body/div[2]/div[6]/div[2]/div[2]/form/footer/span/button")))  # Locate search button
    search_button.click()  # Click on the search button

    # Get the number of courses
    entries_count = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH,
             "/html/body/div[2]/div[6]/div[2]/div[2]/table[2]/tbody/tr/td/table/tbody/tr[3]/td/div/a/b")))  # Locate the entries count element which gives the number of courses
    new_count_courses = entries_count.text  # read the number of courses
    print(new_count_courses)  # print the number of courses

    # Compare the new number of courses with the old number of courses on the file and update the value
    if os.path.exists(
            "status_new_course_notifier.txt"):  # Check if the file that stores the number of current courses exists
        file = open("status_new_course_notifier.txt",
                    "r+")  # Open the existing file in read, write mode
    else:  # If the file that stores the number of courses does not exist
        file = open("status_new_course_notifier.txt",
                    "w+")  # Create the file and open it in write mode
    file_content = file.read()  # Read the contents of the file
    if len(file_content) != 0:  # If the file is not empty
        old_count_courses = file_content  # Read the value of the number of courses on the file
    else:  # If the file is empty
        old_count_courses = 0  # Set the old number of courses to 0
    if int(new_count_courses) > int(
            old_count_courses):  # If the new number of courses is greater than the old number of courses
        file.write(new_count_courses)  # Update the number of courses to the new value
    file.close()  # Close the file after writing

    assert "No results found." not in browser.page_source


check_for_changes()
