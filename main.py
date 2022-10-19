import os
import sys
import subprocess
import time
import signal

from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.options import Options

import helpers
import parser_helper

RECORDING_TIMEOUT_MINS = 1
SLEEP_SECONDS = 5
VERSION = 2.0
HELP_MSG = """Usage: python3 main.py [OPTIONS]...
options:
-h      --help          Print this message and exit
-v      --version       Print version and exit
-i      --input         Enter a course from the course list through stdin
-c=COURSE_ID            Enter a course given a custom id
-t=MINUTES              Set minutes after which the recording will be stopped.
                        Default: 90
"""
COURSE_MAP = {
    "IN0042": "course379",  # IT Sicherheit
    "IN2381": "course391",  # Einführung in Quantum Computing
    "IN0008": "course392",  # Grundlagen Datenbanken
    "IN0009": "course387",  # Grundlagen: Betriebssysteme
}
GECKODRIVER_PATH = "/Library/Frameworks/Python.framework/Versions/3.10/bin/geckodriver"

if __name__ == '__main__':
    # COMMAND FLAGS READING ============================================================================================
    course_id: str = str()
    timeout_minutes: int = RECORDING_TIMEOUT_MINS

    if len(sys.argv) > 3:
        print(HELP_MSG)
        sys.exit(1)

    for arg in sys.argv[1:]:
        match arg.split("="):
            case ["-h"] | ["--help"]:
                print(HELP_MSG)
                sys.exit(0)
            case ["-v"] | ["--version"]:
                print(VERSION)
                sys.exit(0)
            case ["-i"] | ["--input"]:
                course_id = helpers.get_course_class_id(COURSE_MAP)
                continue
            case ["-c", id]:
                course_id = id
                continue
            case ["-t", minutes]:
                timeout_minutes = minutes
                continue
            case _:
                print(HELP_MSG)
                sys.exit(1)

    if not course_id:
        course_id = helpers.get_course_class_id(COURSE_MAP)

    # SETUP ============================================================================================================
    options = Options()
    options.headless = True
    browser = webdriver.WebDriver(options=options, executable_path=GECKODRIVER_PATH)
    browser.get("https://live.rbg.tum.de")

    parser_helper.login(browser)
    parser_helper.enter_course(browser, course_id)
    stream_url: str = parser_helper.get_stream_source(browser)
    browser.quit()

    # MAIN PROCESS =====================================================================================================
    process = subprocess.Popen(
        ["youtube-dl", stream_url],
    )
    try:
        print(f"Running process {process.pid}")
        time.sleep(int(int(timeout_minutes) * 60))
        process.send_signal(signal.SIGINT)
    except Exception as exc:
        print(f"Terminated with exception {exc}")

    time.sleep(SLEEP_SECONDS)

    if not os.path.isdir("./output"):
        os.mkdir("./output")
    subprocess.run(
        ["mv", "./playlist-playlist.mp4.part", helpers.get_filename()]
    )
