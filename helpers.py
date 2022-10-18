

def get_course_class_id(course_map: dict[str, str]) -> str:
    print("f'Select a course ID to see the livestream. Available options: ")
    [print(key) for key in course_map.keys()]
    while (inp := input(": ")) not in course_map.keys():
        print(f"Invalid option: {inp}")

    return course_map[inp]