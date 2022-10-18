from selenium.webdriver.firefox import webdriver
from selenium.webdriver.common.by import By


def login(browser: webdriver):
    login_button = browser.find_element(By.CSS_SELECTOR, "a.inline-block:nth-child(2)")
    login_button.click()
    browser.implicitly_wait(1)
    login_button = browser.find_element(By.CSS_SELECTOR, ".block")
    login_button.click()
    browser.implicitly_wait(1)
    enter_credentials(browser)


def enter_credentials(browser: webdriver):
    CREDENTIALS = {
        "username": "ge95rof",
        "password": open("secrets.txt", "r").read()
    }
    username_input = browser.find_element(By.CSS_SELECTOR, "#username")
    password_input = browser.find_element(By.CSS_SELECTOR, "#password")

    username_input.send_keys(CREDENTIALS["username"])
    password_input.send_keys(CREDENTIALS["password"])

    browser.find_element(By.CSS_SELECTOR, "#btnLogin").click()


def enter_course(browser: webdriver, course_class_id: str):
    found_course = browser.find_element(By.CLASS_NAME, course_class_id)
    found_link = found_course.find_element(By.CSS_SELECTOR, "a:nth-child(1)")
    found_link.click()


def get_stream_source(browser: webdriver) -> str:
    video = browser.find_element(By.CSS_SELECTOR, "#my-video_html5_api > source:nth-child(1)")
    video_url: str = video.get_attribute("src")

    return video_url.replace("live", "edge01").replace("edge01tum", "livetum")