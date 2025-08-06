# remove_employee.py
def remove_employee(employees, name):
    if name in employees:
        employees.remove(name)
    return employees