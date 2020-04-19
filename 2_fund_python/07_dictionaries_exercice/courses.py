student_count = {}
student_names = {}
while True:
    command = input()
    if command == "end":
        break
    course_info = command.split(" : ")
    course_name = course_info[0]
    student_name = course_info[1]

