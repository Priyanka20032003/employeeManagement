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


def update_employee(employee_id, new_department):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            employee["department"] = new_department
            print("Employee updated successfully!")

def delete_employee(employee_id):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            employees.remove(employee)
            print("Employee deleted successfully!")

         

    print("Employee not found")


add_employee(101, "Arun", "IT")
add_employee(102, "Priya", "HR")

view_employees()
search_employee(101)
delete_employee(102)

search_employee(101)

update_employee(101, "Finance")
view_employees()
