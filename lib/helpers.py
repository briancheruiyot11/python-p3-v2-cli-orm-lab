from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# Function to show all departments
def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


# Search for a department by its name
def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


# Search for a department by its ID
def find_department_by_id():
    # Using trailing underscore so we don't overwrite built-in id()
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


# Create a new department
def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


# Update details of an existing department
def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            # Ask user for the new details
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


# Delete a department if it exists
def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# List all employees
def list_employees():
    employees = Employee.get_all()
    for emp in employees:
        print(emp)


# Search an employee by name
def find_employee_by_name():
    name = input("Enter the employee's name: ")
    emp = Employee.find_by_name(name)
    if emp:
        print(emp)
    else:
        print(f"Employee {name} not found")


# Search an employee by ID
def find_employee_by_id():
    try:
        emp_id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid id")
        return
    
    emp = Employee.find_by_id(emp_id)
    if emp:
        print(emp)
    else:
        print(f"Employee {emp_id} not found")


# Create a new employee
def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    dept_id = input("Enter the employee's department id: ")

    try:
        dept_id = int(dept_id)
        emp = Employee.create(name, job_title, dept_id)
        print(f"Success: {emp}")
    except Exception as e:
        print(f"Error creating employee: {e}")


# Update an employee's details
def update_employee():
    try:
        emp_id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid id")
        return

    emp = Employee.find_by_id(emp_id)
    if not emp:
        print(f"Employee {emp_id} not found")
        return

    try:
        # Collect new info from the user
        new_name = input("Enter the employees's new name: ")
        new_title = input("Enter the employee's new job title: ")
        new_dept_id = int(input("Enter the employees's new department id: "))

        emp.name = new_name
        emp.job_title = new_title
        emp.department_id = new_dept_id
        emp.update()

        print(f"Success: {emp}")
    except Exception as e:
        print(f"Error updating employee: {e}")


# Delete an employee
def delete_employee():
    try:
        emp_id = int(input("Enter the employee's id: "))
    except ValueError:
        print("Invalid id")
        return

    emp = Employee.find_by_id(emp_id)
    if emp:
        emp.delete()
        print(f"Employee {emp_id} deleted")
    else:
        print(f"Employee {emp_id} not found")


# List all employees of a specific department
def list_department_employees():
    try:
        dept_id = int(input("Enter the department's id: "))
    except ValueError:
        print("Invalid id")
        return

    dept = Department.find_by_id(dept_id)
    if not dept:
        print(f"Department {dept_id} not found")
        return

    # Show each employee in the department
    employees = dept.employees()
    for emp in employees:
        print(emp)
