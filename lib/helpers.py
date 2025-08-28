from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# Department functions

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# Employee functions

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        print(employee)
    else:
        print(f"Employee {id_} not found")


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")
    try:
        employee = Employee(name=name, job_title=job_title, department_id=department_id)
        employee.save()
        print(f"Success: {employee}")
    except Exception as exc:
        print(f"Error creating employee: {exc}")


def update_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        try:
            new_name = input("Enter the employee's new name: ")
            employee.name = new_name
            new_job_title = input("Enter the employee's new job title: ")
            employee.job_title = new_job_title
            new_department_id = input("Enter the employee's new department id: ")
            employee.department_id = new_department_id

            employee.update()
            print(f"Success: {employee}")
        except Exception as exc:
            print(f"Error updating employee: {exc}")
    else:
        print(f"Employee {id_} not found")


def delete_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")


def list_department_employees():
    dept_id = input("Enter the department's id: ")
    department = Department.find_by_id(dept_id)
    if department:
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f"Department {dept_id} not found")
