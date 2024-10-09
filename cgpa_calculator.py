import pandas

semester_gpa = {'Semester No': [], 'GPA': [], 'Semester Marks': [], 'Total Credit Hours': [], 'Subjects': []}

b_grade_range = {70: 3.0, 71: 3.1, 72: 3.2, 73: 3.3, 74: 3.4, 75: 3.5, 76: 3.6, 77: 3.7, 78: 3.8, 79: 3.9}

c_grade_range = {60: 2.0, 61: 2.1, 62: 2.2, 63: 2.3, 64: 2.4, 65: 2.5, 66: 2.6, 67: 2.7, 68: 2.8, 69: 2.9}

d_grade_range = {50: 1.0, 51: 1.1, 52: 1.2, 53: 1.3, 54: 1.4, 55: 1.5, 56: 1.6, 57: 1.7, 58: 1.8, 59: 1.9}


def format_cgpa(culminativegpa):  # made this function to round off the number at [4] so that 3.125 becomes 3.13
    # if we used round function it would have become 3.12 as round rounds off to
    # even number
    cgpa = "{:.3f}".format(culminativegpa)
    if int(cgpa[4]) >= 5:
        cgpa = cgpa.replace(cgpa[3], (str(int(cgpa[3]) + 1)))
        cgpa = cgpa[:-1]
    else:
        pass
    return float(cgpa)


def make_cgpa():
    name = input("Enter Your Name:\n")
    semester_count = int(input("How many semesters?\n\n"))
    semester = 1
    while semester_count != 0:

        points = []
        credit_hour = input("Enter Subject Credit Hours separated by Comma:\n\n").split(", ")
        credit_hour = [eval(credit) for credit in credit_hour]
        subjects = len(credit_hour)
        total_credit_hours = sum(credit_hour)
        print(f"Credit Hours for Semester {semester} have been entered with {subjects} subjects")
        marks = input("Enter Your Marks separated by Comma:\n\n").split(", ")
        marks = [eval(mark) for mark in marks]
        print(f"Marks for Semester {semester} have been entered with {subjects} subjects")
        for num in range(subjects):
            if marks[num] > 79:
                points.append(4.0)
            elif marks[num] < 50:
                points.append(0.0)
            elif marks[num] in b_grade_range:
                points.append(b_grade_range[marks[num]])
            elif marks[num] in c_grade_range:
                points.append(c_grade_range[marks[num]])
            elif marks[num] in d_grade_range:
                points.append(d_grade_range[marks[num]])
        quality_points = [(points[elements] * credit_hour[elements]) for elements in range(subjects)]
        gpa = sum(quality_points) / total_credit_hours
        gpa = round(gpa, 2)
        print(
            f"GPA for Semester {semester} is: {gpa} and Total credit hours for this semester are: {total_credit_hours}\n")
        semester_gpa['Semester No'].append(semester)
        semester_gpa['GPA'].append(gpa)
        semester_gpa['Semester Marks'].append((sum(marks)))
        semester_gpa['Total Credit Hours'].append(total_credit_hours)
        semester_gpa['Subjects'].append(subjects)
        semester += 1
        semester_count -= 1

    print(
        f"Total Credit Hours for {len(semester_gpa['Subjects'])} Semester(s) are {sum(semester_gpa['Total Credit Hours'])}")

    total_gpa = sum(semester_gpa['GPA'])
    total_gpa = round(total_gpa)
    print(f"total gpa: {total_gpa}")
    total_marks = (sum(semester_gpa['Subjects'])) * 100
    obtained_marks = (sum(semester_gpa['Semester Marks']))
    percentage = (obtained_marks / total_marks) * 100
    percentage_rounded = round(percentage, 2)
    cgpa = (total_gpa / len(semester_gpa['Semester No']))
    cgpa2 = (total_gpa / int(subjects))
    cgpa2 = round(cgpa2, 2)
    cgpa = round(cgpa, 2)
    print(f"\n Your CGPA is: {cgpa}")
    print(f"\n Your Obtained Marks are: {obtained_marks}, Your Percentage is: {percentage_rounded}")

    df = pandas.DataFrame.from_dict(semester_gpa)
    print(df)
    # df.to_csv(f"{name}.csv", index=False) # uncomment if you want to save output as a CSV

'''
This portion is commented but it is intended to make cgpa and gpa from a CSV

def from_csv(csv):
    df2 = pandas.read_csv(csv)
    read_csv_dict = df2.to_dict()
    semester_no = [semester_no for semester_no in read_csv_dict['Semester No'].values()]
    gpa = [gpa_points for gpa_points in read_csv_dict['GPA'].values()]
    marks = [mark for mark in read_csv_dict['Semester Marks'].values()]
    credit_hours = [credit for credit in read_csv_dict['Total Credit Hours'].values()]
    subjects = [subject for subject in read_csv_dict['Subjects'].values()]

    semester_gpa['Semester No'] = semester_no
    semester_gpa['GPA'] = gpa
    semester_gpa['Semester Marks'] = marks
    semester_gpa['Total Credit Hours'] = credit_hours
    semester_gpa['Subjects'] = subjects

    total_gpa = sum(semester_gpa['GPA'])
    total_gpa = round(total_gpa, 0)
    total_marks = (sum(semester_gpa['Subjects'])) * 100
    obtained_marks = (sum(semester_gpa['Semester Marks']))
    percentage = (obtained_marks / total_marks) * 100
    percentage_rounded = round(percentage, 2)

    cgpa = (total_gpa / len(semester_gpa['Semester No']))
    cgpa = format_cgpa(cgpa)
    print(
        f"Your CGPA is: {cgpa} and Your Obtained Marks are: {obtained_marks}, Your Percentage is: {percentage_rounded}")
    print(
        f"Total Credit Hours for {len(semester_gpa['Subjects'])} Semesters are {sum(semester_gpa['Total Credit Hours'])}")

'''
make_cgpa()
