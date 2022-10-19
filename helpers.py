from datetime import datetime


def get_course_class_id(course_map: dict[str, str]) -> str:
    print("Select a course ID to see the livestream. Available options: ")
    [print(key) for key in course_map.keys()]
    while (inp := input(": ")) not in course_map.keys():
        print(f"Invalid option: {inp}")

    return course_map[inp]


def get_filename() -> str:
    now = datetime.now()
    return f"./output/{now.year}.{now.month}.{now.day}-{now.hour}.{now.minute}_aufzeichnung.mp4"