class Employee: 

    def __init__(self):
        self.name = "",
        self.job_title = ""
        self.start_date = ""

class Company: 

    def __init__(self):
        self.company_name = "",
        self.address = "",
        self.business_type = ""
        self.employees = list()


Fony = Company()
Fony.company_name = "Fony"
Fony.business_type = "electronics"

Macrosoft = Company()
Macrosoft.company_name = "Macrosoft"
Macrosoft.business_type = "software"

employee_1 = Employee()
employee_1.name = "Shane Miller"

employee_2 = Employee()
employee_2.name = "Krystal Gates"

employee_3 = Employee()
employee_3.name = "Jake Scott"

employee_4 = Employee()
employee_4.name = "Chris Balma"

employee_5 = Employee()
employee_5.name = "Peter Parker"

Fony.employees.append(employee_5)
Fony.employees.append(employee_3)

Macrosoft.employees.append(employee_1)
Macrosoft.employees.append(employee_2)
Macrosoft.employees.append(employee_4)

print(f"{Fony.company_name}, which is involved in {Fony.business_type} has the following employees:")

for employee in Fony.employees:
    print(f"* {employee.name}" )

print(f"{Macrosoft.company_name}, which is involved in {Macrosoft.business_type} has the following employees:")

for employee in Macrosoft.employees:
    print(f"* {employee.name}" )


