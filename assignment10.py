employee_ids = ["EMP001", "EMP002", "EMP003", "EMP004", "EMP005"]
employee_data = []

print("Initial IDs:", employee_ids)
print("Initial Employee Data:", employee_data)
print()

def add_employee(name, age, salary, is_manager, skills):
    if len(employee_data) < len(employee_ids):
        employee = {
            "Name": name,
            "Age": age,
            "Salary": salary,
            "Is_Manager": is_manager,
            "Skills": skills,
            "ID": employee_ids[len(employee_data)]
        }
        employee_data.append(employee)

def get_average_salary():
    total = 0
    for emp in employee_data:
        total += emp["Salary"]
    return total / len(employee_data)

def list_managers():
    managers = []
    for emp in employee_data:
        if emp["Is_Manager"]:
            managers.append(emp["Name"])
    return managers

def get_employees_by_skill(skill):
    result = []
    for emp in employee_data:
        if skill in emp["Skills"]:
            result.append(emp["Name"])
    return result

def delete_employee(emp_id):
    for emp in employee_data:
        if emp["ID"] == emp_id:
            employee_data.remove(emp)
            break

add_employee("Mohan", 24, 70000.0, True, ["Python", "Leadership"])
add_employee("Rohan", 38, 50000.0, False, ["Excel", "Communication"])
add_employee("Rishab", 42, 90000.0, True, ["Project Management", "Java"])
add_employee("Spurti", 25, 40000.0, False, ["Python", "Problem Solving"])
add_employee("Divya", 29, 60000.0, False, ["Excel", "Python"])

print("Added Employees:", [e["Name"] for e in employee_data])
print()

print("Before Deletion:", [e["ID"] for e in employee_data])
delete_employee("EMP005")
print("After Deletion of EMP005:", [e["ID"] for e in employee_data])
print()

print("Average Salary:", get_average_salary())
print()

print("Managers:", list_managers())
print()

print("Employees with Python:", get_employees_by_skill("Python"))
print()

above_30 = []
for emp in employee_data:
    if emp["Age"] > 30:
        above_30.append(emp["Name"])
print("Employees above 30:", above_30)
print()

all_skills = []
for emp in employee_data:
    all_skills.extend(emp["Skills"])
unique_skills = list(set(all_skills))
print("Unique Skills:", unique_skills)
print()

total_age = 0
for emp in employee_data:
    total_age += emp["Age"]
average_age = total_age / len(employee_data)
print("Average Age:", round(average_age, 1))
print()

highest_paid = employee_data[0]
for emp in employee_data:
    if emp["Salary"] > highest_paid["Salary"]:
        highest_paid = emp
print("Highest Paid Employee:", highest_paid["Name"])
print()

skill_counts = {}
for emp in employee_data:
    for skill in emp["Skills"]:
        if skill in skill_counts:
            skill_counts[skill] += 1
        else:
            skill_counts[skill] = 1
print("Skill Counts:", skill_counts)
print()

print("Final Summary")
print("Total Employees:", len(employee_data))
print("Average Salary:", get_average_salary())
print("Managers:", list_managers())
print("Employees with 'Python':", get_employees_by_skill("Python"))
print("Employees above 30:", above_30)
print("Unique Skills:", unique_skills)
print("Average Age:", round(average_age, 1))
print("Highest Paid Employee:", highest_paid["Name"])
print("Skill Counts:", skill_counts)