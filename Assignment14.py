# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.emp_id}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()


emp1 = Employee("Aiza", 101)

dept1 = Department("HR", emp1)

dept1.show_details()
