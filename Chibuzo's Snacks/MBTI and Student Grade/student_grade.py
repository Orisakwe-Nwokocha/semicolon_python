grades = []


def set_grades(multidimensional_list):
    grades.extend(multidimensional_list)


def input_grades():
    students_row = int(input("How many students do you have?\n"))
    while students_row <= 0:
        students_row = int(input("Invalid input\nHow many students do you have?\n"))

    subjects_column = int(input("How many subjects do they offer?\n"))
    while subjects_column <= 0:
        subjects_column = int(input("Invalid input\nHow many subjects do they offer?:\n"))

    print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nSaved successfully\n")

    for student in range(students_row):
        row = []
        for subject in range(subjects_column):
            print(f"Entering score for student {student + 1}")
            score = int(input(f"Enter score for subject {subject + 1}\n"))
            while score < 0 or score > 100:
                print(f"Invalid score\n\nEntering score for student {student + 1}")
                score = int(input(f"Enter score for subject {subject + 1}\n"))

            print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>>\nSaved successfully\n")
            row.append(score)
        grades.append(row)


def get_total(students_list):
    total = 0

    for scores in students_list:
        total += scores

    return total


def get_average(students_list):
    average = 0

    for scores in students_list:
        average += scores

    return average / len(students_list)


def get_position(students_list):
    average = 0
    position = 1

    for scores in students_list:
        average += scores

    average = average / len(students_list)

    for students in grades:
        if average < get_average(students):
            position += 1

    return position


def output_grades():
    print("===============================================================================")
    print("STUDENT           ", end="")

    for subject in range(len(grades[0])):
        print(f"SUB{subject + 1}    ", end="")

    print(" TOT     AVE     POS")
    print("===============================================================================")

    for student in range(len(grades)):
        print(f"Student {student + 1}          ", end="")

        for subject in grades[student]:
            print(f"{subject}      ", end="")

        total = get_total(grades[student])
        average = get_average(grades[student])
        student_position = get_position(grades[student])

        print(f"{total}    {average:.2f}     {student_position}")

        print()

    print("===============================================================================")
    print("===============================================================================\n")


def get_highest_score(subject):
    highest_score = 0
    for student in grades:
        if student[subject] > highest_score:
            highest_score = student[subject]

    return highest_score


def get_lowest_score(subject):
    lowest_score = get_highest_score(subject)
    for student in grades:
        if student[subject] < lowest_score:
            lowest_score = student[subject]

    return lowest_score


def get_total_score(subject):
    total_score = 0
    for student in grades:
        total_score += student[subject]

    return total_score


def no_of_passes(subject):
    passes = 0
    for student in grades:
        if student[subject] >= 50:
            passes += 1

    return passes


def no_of_failures(subject):
    fails = 0
    for student in grades:
        if student[subject] < 50:
            fails += 1

    return fails


def get_hardest_subject():
    fails = 0
    hardest_subject = 0

    for student in range(len(grades)):
        for subject in range(len(grades[0])):
            if no_of_failures(subject) > fails:
                hardest_subject = subject + 1
                fails = no_of_failures(subject)

    if fails > 0:
        print(f"The hardest subject is Subject {hardest_subject} with {fails} failures")
    else:
        print("There are apparently no hard subjects because there are 0 failures")


def get_easiest_subject():
    passes = 0
    easiest_subject = 0

    for student in range(len(grades)):
        for subject in range(len(grades[0])):
            if no_of_passes(subject) > passes:
                easiest_subject = subject + 1
                passes = no_of_passes(subject)

    if passes > 0:
        print(f"The easiest subject is Subject {easiest_subject} with {passes} passes")
    else:
        print("There are apparently no easy subjects because there are 0 passes")


def get_overall_highest_score():
    overall_highest_score = grades[0][0]
    overall_highest_scoring_student = 0
    subject_scored_in = 0

    for student in range(len(grades)):
        for subject in range(len(grades[0])):
            if grades[student][subject] > overall_highest_score:
                overall_highest_scoring_student = student + 1
                subject_scored_in = subject + 1
                overall_highest_score = grades[student][subject]

    if overall_highest_score > 0:
        print(f"The overall Highest score is scored by Student {overall_highest_scoring_student} "
              f"in subject {subject_scored_in} scoring {overall_highest_score}")
    else:
        print("All scores were 0, so there is no overall Highest score")


def get_overall_lowest_score():
    overall_lowest_score = grades[0][0]
    overall_lowest_scoring_student = 0
    subject_scored_in = 0

    for student in range(len(grades)):
        for subject in range(len(grades[0])):
            if grades[student][subject] < overall_lowest_score:
                overall_lowest_scoring_student = student + 1
                subject_scored_in = subject + 1
                overall_lowest_score = grades[student][subject]

    if overall_lowest_score > 0:
        print(f"The overall Lowest score is scored by Student {overall_lowest_scoring_student} "
              f"in subject {subject_scored_in} scoring {overall_lowest_score}")
    else:
        print("All scores were 0, so there is no overall Lowest score")


def subject_summary():
    print("SUBJECT SUMMARY")

    for subject in range(len(grades[0])):
        print(f"Subject {subject + 1}")

        highest_scoring_student = 0
        for student in range(len(grades)):
            if get_highest_score(subject) == grades[student][subject]:
                highest_scoring_student = student + 1

        lowest_scoring_student = 0
        for student in range(len(grades)):
            if get_lowest_score(subject) == grades[student][subject]:
                lowest_scoring_student = student + 1

        print(f"""Highest scoring student is: Student {highest_scoring_student} scoring {get_highest_score(subject)}
Lowest scoring student is: Student {lowest_scoring_student} scoring {get_lowest_score(subject)}
Total score is:  {get_total_score(subject)}
Average score is: {get_total_score(subject) / len(grades):.2f}
Number of passes: {no_of_passes(subject)}
Number of fails: {no_of_failures(subject)}""")

        print()

    get_hardest_subject()
    get_easiest_subject()
    get_overall_highest_score()
    get_overall_lowest_score()


    print("===============================================================================\n")


def class_summary():
    print("CLASS SUMMARY")
    print("===============================================================================")

    best_graduating_student = 0
    best_total_grade = 0

    for student in range(len(grades)):
        for subject in range(len(grades[0])):
            if get_total(grades[student]) > best_total_grade:
                best_graduating_student = student + 1
                best_total_grade = get_total(grades[student])

    if best_total_grade > 0:
        print(f"Best Graduating Student is: Student {best_graduating_student} scoring {best_total_grade}")
    else:
        print("All scores were 0, so there is no Best Graduating Student")

    print("===============================================================================\n")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    worst_graduating_student = 0
    worst_total_grade = best_total_grade

    for student in range(len(grades)):
        for subject in range(len(grades[0])):
            if get_total(grades[student]) < worst_total_grade:
                worst_graduating_student = student + 1
                worst_total_grade = get_total(grades[student])

    if worst_total_grade > 0:
        print(f"Worst Graduating Student is: Student {worst_graduating_student} scoring {worst_total_grade}")
    else:
        print("All scores were 0, so there is no Worst Graduating Student")

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

    print("===============================================================================")

    class_total_score = 0
    for subject in range(len(grades[0])):
        class_total_score += get_total_score(subject)
    print(f"Class Total score is: {class_total_score}")
    print(f"Class Average score is: {class_total_score / len(grades):.2f}")

    print("===============================================================================\n")


def process_grades():
    output_grades()
    subject_summary()
    class_summary()
