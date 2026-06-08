def calculate_fitness(chromosome, students, courses, slots):

    penalty = 0

    penalty += same_slot_conflicts(chromosome, students, courses)

    penalty += same_day_penalty(chromosome, students, courses, slots)

    penalty += consecutive_days_penalty(chromosome, students, courses, slots)

    penalty += used_days_penalty(chromosome, slots)

    fitness = 1 / (1 + penalty)

    chromosome.fitness = fitness

    return fitness


def same_slot_conflicts(chromosome, students, courses):

    penalty = 0

    course_index = {}

    for index, course in enumerate(courses):

        course_index[course.course_code] = index

    for student in students:

        student_courses = student.courses

        for i in range(len(student_courses)):

            for j in range(i + 1, len(student_courses)):

                course1 = student_courses[i]
                course2 = student_courses[j]

                slot1 = chromosome.genes[course_index[course1]]

                slot2 = chromosome.genes[course_index[course2]]

                if slot1 == slot2:

                    penalty += 1000

    return penalty


def same_day_penalty(chromosome, students, courses, slots):

    penalty = 0

    course_index = {}

    for index, course in enumerate(courses):

        course_index[course.course_code] = index

    for student in students:

        day_counts = {}

        for course_code in student.courses:

            gene_index = course_index[course_code]

            slot_number = chromosome.genes[gene_index]

            slot = slots[slot_number - 1]

            day = slot.exam_day

            if day not in day_counts:

                day_counts[day] = 0

            day_counts[day] += 1

        for exams_count in day_counts.values():

            if exams_count > 2:

                penalty += 800

            elif exams_count == 2:

                penalty += 50

    return penalty


def consecutive_days_penalty(chromosome, students, courses, slots):

    penalty = 0

    course_index = {}

    for index, course in enumerate(courses):

        course_index[course.course_code] = index

    for student in students:

        day_counts = {}

        for course_code in student.courses:

            gene_index = course_index[course_code]

            slot_number = chromosome.genes[gene_index]

            slot = slots[slot_number - 1]

            day = slot.exam_day

            if day not in day_counts:

                day_counts[day] = 0

            day_counts[day] += 1

        for day in range(1, 6):

            exams_in_two_days = day_counts.get(day, 0) + day_counts.get(day + 1, 0)

            if exams_in_two_days >= 4:

                penalty += 500

    return penalty


def used_days_penalty(chromosome, slots):

    penalty = 0

    used_days = set()

    for slot_number in chromosome.genes:

        slot = slots[slot_number - 1]

        used_days.add(slot.exam_day)

    used_days_count = len(used_days)

    preferred_days = 5

    if used_days_count > preferred_days:

        penalty += (used_days_count - preferred_days) * 100

    return penalty
