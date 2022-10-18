from selenium.webdriver.firefox import webdriver

import helpers
import parser_helper

COURSE_MAP = {
    "IN0042": "course379"
}

if __name__ == '__main__':
    # SETUP ============================================================================================================
    browser = webdriver.WebDriver(executable_path="/Library/Frameworks/Python.framework/Versions/3.10/bin/geckodriver")
    browser.get("https://live.rbg.tum.de")

    parser_helper.login(browser)
    parser_helper.enter_course(browser, helpers.get_course_class_id(COURSE_MAP))

    print(parser_helper.get_stream_source(browser))

    # MAIN LOOP ========================================================================================================
    while True:
        pass

