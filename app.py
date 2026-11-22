employees = []


def add_employee(employee_id, name, department):
    employee = {
        "employee_id": employee_id,
        "name": name,
        "department": department
    }

    employees.append(employee)
    print("Employee added successfully!")


def view_employees():
    for employee in employees:
        print(employee)


def search_employee(employee_id):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            print("Employee found:", employee)
            return

    print("Employee not found")

Print("Hello")


add_employee(101, "Arun", "IT")
add_employee(102, "Priya", "HR")

view_employees()

search_employee(101)
