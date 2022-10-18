import os
import sys

from selenium.webdriver.firefox import webdriver

import helpers
import parser_helper

VERSION = 1.1
HELP_MSG = """Usage: python3 main.py [OPTIONS]...
options:
-h      --help          Print this message and exit
-v      --version       Print version and exit
-i      --input         Enter a course from the course
"""
COURSE_MAP = {
    "IN0042": "course379"
}
GECKODRIVER_PATH = "/Library/Frameworks/Python.framework/Versions/3.10/bin/geckodriver"

if __name__ == '__main__':
    # COMMAND FLAGS READING ============================================================================================
    for arg in sys.argv[1:]:
        match arg.split("="):
            case ["-h"] | ["--help"]:
                print(HELP_MSG)
                sys.exit(0)
            case ["-v"] | ["--version"]:
                print(VERSION)
                sys.exit(0)



    # SETUP ============================================================================================================
    browser = webdriver.WebDriver(executable_path=GECKODRIVER_PATH)
    browser.get("https://live.rbg.tum.de")

    parser_helper.login(browser)
    #parser_helper.enter_course(browser, helpers.get_course_class_id(COURSE_MAP))
    parser_helper.enter_course(browser, "course465")
    stream_url: str = parser_helper.get_stream_source(browser)

    # MAIN LOOP ========================================================================================================


    os.system(f"youtube-dl {stream_url}")

    while True:
        pass

