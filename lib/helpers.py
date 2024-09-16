from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


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
    # use a trailing underscore not to override the built-in id function
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


# You'll implement the employee functions in the lab

def list_employees():
        try:
            employees = Employee.query.all()  # Replace with the appropriate ORM call to get all employees
            for employee in employees:
                print(employee)
        except Exception as e:
            print(f"Error retrieving employees: {e}")



def find_employee_by_name():
    name = input("Enter the employee's name: ")
    try:
        employee = Employee.query.filter_by(name=name).first()  # Replace with the ORM call to find an employee by name
        if employee:
            print(employee)
        else:
            print(f"Employee {name} not found")
    except Exception as e:
        print(f"Error finding employee by name: {e}")



def find_employee_by_id():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.query.get(employee_id)  # Replace with the ORM call to find an employee by ID
        if employee:
            print(employee)
        else:
            print(f"Employee {employee_id} not found")
    except ValueError:
        print("Invalid ID format")
    except Exception as e:
        print(f"Error finding employee by id: {e}")


def create_employee():
    try:
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        department_id = int(input("Enter the employee's department id: "))
        
        # Validate department_id
        department = Department.query.get(department_id)
        if not department:
            print("Error creating employee: department_id must reference a department in the database")
            return
        
        # Create and save the employee
        employee = Employee(name=name, job_title=job_title, department_id=department_id)
        employee.save()  # Replace with the ORM call to save the employee
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error creating employee: {e}")
    except Exception as e:
        print(f"Error creating employee: {e}")


def update_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.query.get(employee_id)  # Replace with the ORM call to find employee by ID
        
        if not employee:
            print(f"Employee {employee_id} not found")
            return
        
        name = input("Enter the employee's new name: ")
        job_title = input("Enter the employee's new job title: ")
        department_id = int(input("Enter the employee's new department id: "))
        
        # Validate department_id
        department = Department.query.get(department_id)
        if not department:
            print("Error updating employee: department_id must reference a department in the database")
            return
        
        # Update and save the employee
        employee.name = name
        employee.job_title = job_title
        employee.department_id = department_id
        employee.save()  # Replace with the ORM call to update the employee
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error updating employee: {e}")
    except Exception as e:
        print(f"Error updating employee: {e}")



def delete_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.query.get(employee_id)  # Replace with the ORM call to find employee by ID
        
        if not employee:
            print(f"Employee {employee_id} not found")
            return
        
        # Delete the employee
        employee.delete()  # Replace with the ORM call to delete the employee
        print(f"Employee {employee_id} deleted")
    except ValueError:
        print("Invalid ID format")
    except Exception as e:
        print(f"Error deleting employee: {e}")



def list_department_employees():
    try:
        department_id = int(input("Enter the department's id: "))
        department = Department.query.get(department_id)  # Replace with the ORM call to find department by ID
        
        if not department:
            print(f"Department {department_id} not found")
            return
        
        employees = department.employees()  # Replace with the ORM call to get employees in the department
        for employee in employees:
            print(employee)
    except ValueError:
        print("Invalid ID format")
    except Exception as e:
        print(f"Error retrieving department employees: {e}")
