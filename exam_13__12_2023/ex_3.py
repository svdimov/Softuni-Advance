def softuni_students(*args, **courses):

    students = {}

    invalid_course = []
    for st_id , st_names in args:
        if st_id in courses:
            course_names = courses[st_id]
            students[st_names] = course_names
        else:
            invalid_course.append(st_names)
    sorted_student = sorted(students.items())

    result = []
    for student,course in sorted_student:
        result.append(f"*** A student with the username {student} has successfully finished the course {course}!")

    if invalid_course:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid_course))}")

    return "\n".join(result)

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))