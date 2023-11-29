#Exercise:
class Emploee:
    
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def calculate_emp_salary(self, salary, hours_worked):
        while 1:
            if hours_worked < 0:
                print("Error: Invalid input for worked hours")
                hours_worked = float(input("Enter worked hours: "))
            else:
                break
            
        if hours_worked > 50 :
            overtime = hours_worked - 50
            overtime_amount = overtime * (salary/50)
            self.emp_salary = overtime_amount + salary
        else:
            self.emp_salary = salary
    
    def emp_asign_apartment(self, new_apartment):
        self.emp_department = new_apartment
        
        
    def print_emp_details(self):
        print(f"ID: {self.emp_id}, Name: {self.emp_name}, Salary: {self.emp_salary}, Department: {self.emp_department}")
        
        
    
e1 = Emploee(1, "Alia", 1800, "IT")
e2 = Emploee(2, "Sara", 1000, "Accounting")
e1.print_emp_details()
e2.print_emp_details()
print()
e2.calculate_emp_salary(1000, -90)
e2.emp_asign_apartment("IT")
e2.print_emp_details()
print()
e1.calculate_emp_salary(1800, 50)
e1.emp_asign_apartment("Security")
e1.print_emp_details()








