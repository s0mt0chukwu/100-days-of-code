#
#     total
#     average
#
# }

def result_compiler():
    students_name = input("Enter the name of the student: ")
    english = int(input("Enter the students English score: "))
    maths = int(input("Enter the students Maths score: "))
    physics = int(input("Enter the students Physics score: "))
    chemistry = int(input("Enter the students Chemistry score: "))
    biology = int(input("Enter the students Biology score: "))
    total = english + maths + physics + chemistry + biology
    print(f"{students_name}'s Total score is {total}.")
    average = total / 5
    print(f"{students_name}'s Average score is {average}.")

    results = {
        "student_name": students_name,
        "english_score": english,
        "maths_score": maths,
        "physics_score": physics,
        "chemistry_score": chemistry,
        "biology_score": biology,
        "total_score": total,
        "average_score": average
    }
    return results


all_students_data = []
should_continue = True

while should_continue:
    current_students = result_compiler()
    all_students_data.append(current_students)
    continue_again = input("Do you want to calculate the result of another student? 'y' or 'n': ").lower()
    if continue_again.lower() == "n":
        should_continue = False

print("\n FINAL STUDENT'S RESULTS")
for student in all_students_data:
    print(
        f"{student['student_name']}, "
        f"English: {student['english_score']}, "
        f"Maths: {student['maths_score']}, "
        f"Physics: {student['physics_score']}, "
        f"Chemistry: {student['chemistry_score']},"
        f" Biology: {student['biology_score']}, "
        f"Total: {student['total_score']}, "
        f"Average: {student['average_score']} "
    )
