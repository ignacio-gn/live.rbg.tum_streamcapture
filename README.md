# live.rbg.tum streamcapture
Capture livestreams from TUM and store them locally

## Dependencies
This tool uses bash and Python 3.10 or later.
### Python dependencies
- Selenium 4.3.0
- youtube-dl 2021.12.17

### Other dependencies
- Firefox
- geckodriver

## Installation
After installing all necessary dependencies, write a JSON file at ./secrets.json containing the values for the following keys:
- username: [tum username]
- password: [tum password]

Example file: 
{
    "username": "tu00usr",
    "password": "mypassword"
}

## Setup 
Make sure to set the following important environment variables:
- GECKODRIVER_PATH: Default is "/Library/Frameworks/Python.framework/Versions/3.10/bin/geckodriver" 
- COURSE_MAP: Courses with the given class name as to be found on live.rbg.in.tum.de

## Usage
Details on flags can be found with the -f option.
Output is stored on ./output with the date and time of the recording as filename and on .mp4 format.

## Misc
TODO
