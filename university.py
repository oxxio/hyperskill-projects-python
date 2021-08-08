
maximum_for_department = int(input())

applicants = []
departments = []
with open("applicant_list_7.txt", "r") as file:
    for line in file.readlines():
        line_data = line.split()
        applicant = {"firstname": line_data[0],
                     "lastname": line_data[1],
                     "fullname": line_data[0] + " " + line_data[1],
                     "exams": {"physics": float(line_data[2]),
                               "chemistry": float(line_data[3]),
                               "math": float(line_data[4]),
                               "computer science": float(line_data[5]),
                               "special": float(line_data[6])},
                     "departments": {"A": line_data[7],
                                     "B": line_data[8],
                                     "C": line_data[9]}}
        applicants.append(applicant)
        if line_data[7] not in departments:
            departments.append(line_data[7])
        if line_data[8] not in departments:
            departments.append(line_data[8])
        if line_data[9] not in departments:
            departments.append(line_data[9])

departments.sort()

departments_students = dict.fromkeys(departments)
departments_exams = dict.fromkeys(departments)
departments_exams["Physics"] = ["physics", "math"]
departments_exams["Chemistry"] = "chemistry"
departments_exams["Mathematics"] = "math"
departments_exams["Engineering"] = ["computer science", "math"]
departments_exams["Biotech"] = ["chemistry", "physics"]

priorities = ["A", "B", "C"]


def average_score(exam_results, disciplines):
    finals = 0
    if isinstance(disciplines, str):
        finals = exam_results.get(disciplines)
    else:
        sum_ = 0
        for discipline in disciplines:
            sum_ += exam_results.get(discipline)
        finals = round(sum_ / len(disciplines), 1)
    return max(finals, exam_results["special"])


def sorter(x):
    return -average_score(x["exams"], departments_exams.get(department)), x["fullname"]
# sorter = lambda x: (-x["exams"][departments_exams.get(department)], x["fullname"])


for priority in priorities:
    for department in departments:
        all_applicants_to_department = [x for x in applicants if x.get("departments").get(priority) == department]
        all_applicants_to_department.sort(key=sorter)

        for el in all_applicants_to_department[:maximum_for_department]:
            if departments_students.get(department) is None:
                departments_students[department] = list()
            if len(departments_students[department]) < maximum_for_department:
                applicants.remove(el)
                departments_students[department].append(el)

for department, students in departments_students.items():
    with open(department.lower() + ".txt", "w") as file:
        # print(department, file=file)
        students.sort(key=sorter)
        for student in students:
            print(student["fullname"], average_score(student["exams"], departments_exams.get(department)), file=file)

