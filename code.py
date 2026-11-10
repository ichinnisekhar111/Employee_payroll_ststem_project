class Admin:
    def is_empty(self):
        with open('employees.txt','r') as f:
            data = f.readlines()
        if len(data) == 0:
            return True
        else:
            return False
            
    def read_employees(self):
        with open('employees.txt','r') as f:
            data = f.readlines()
        return data
        
    def check_employee(self,emp_id):
        with open('employees.txt','r') as f:
            data = f.readlines()

        is_found = False
        for line in data:
            details = line.strip().split(',')
            if emp_id == int(details[0]):
                is_found = True
        return is_found


    def add_employee(self):
        emp_id = int(input("Enter Employee ID : "))
        if self.check_employee(emp_id):
            print("Employee with this ID already Exist !")
            return
        name = input("Enter Employee Name : ")
        role = input("Enter Role : ")

        print("\nSelect job type")
        print("1. Full Time Employee")
        print("2. Part Time Employee")
        choice_2 = int(input())
        if choice_2 == 1:
            job_type = 'full_time'
            working_hours = 'NA'
            part_time_sal = 'NA'
            salary = int(input("Enter Employee salary : "))
            with open('employees.txt','a') as f:
                f.write(f"{emp_id},{name},{role},{job_type},{working_hours},{part_time_sal},{salary}\n")
            
            tax = int(0.05 * salary)
            bonus = 0
            final_salary = int((salary - tax) + bonus)
            with open('payroll.txt','a') as f:
                f.write(f"{emp_id},{salary},{tax},{bonus},{final_salary}\n")

        else:
            job_type = 'part_time'
            working_hours = int(input("Enter No of Working hours : "))
            part_time_sal = int(input("Enter salary per Hour : "))
            salary = 'NA'
            with open('employees.txt','a') as f:
                f.write(f"{emp_id},{name},{role},{job_type},{working_hours},{part_time_sal},{salary}\n")

            salary = int(working_hours * part_time_sal)
            tax = int(0.05 * salary)
            bonus = 0
            final_salary = int((salary - tax) + bonus)
            with open('payroll.txt','a') as f:
                f.write(f"{emp_id},{salary},{tax},{bonus},{final_salary}\n")

        print("Employee added successfully")


    def remove_employee(self):
        is_empty = self.is_empty()
        if is_empty:
            print("No employee Records found in Database ")
        else:
            emp_id = int(input("Enter Employee ID : "))
            is_found = self.check_employee(emp_id)
            if is_found:
                data = self.read_employees()
                with open('employees.txt','w') as f:
                    for line in data:
                        details = line.strip().split(',')
                        if emp_id == int(details[0]):
                            pass
                        else:
                            f.write(line)

                with open("payroll.txt",'r') as f:
                    data = f.readlines()
                with open('payroll.txt','w') as f:
                    for line in data:
                        details = line.strip().split(',')
                        if emp_id == int(details[0]):
                            pass
                        else:
                            f.write(line)

                print("Employee Removed from Database")
            else:
                print("Employee Not Found ")


    def view_employee(self):
        is_empty = self.is_empty()
        if is_empty:
            print("No employee Records found in Database ")
        else:
            emp_id = int(input("Enter Employee ID : "))
            emp_status = self.check_employee(emp_id)
            if emp_status:
                data = self.read_employees()
                for line in data:
                    details = line.strip().split(',')
                    if emp_id == int(details[0]):
                        print("---------------------------------------------------------------------------------")
                        print(f"|Emp Name  |Role        |Job type       |Working Hours  |Salary / h  |Salary    |")
                        print("---------------------------------------------------------------------------------")
                        print(f"|{details[1] + ' '*(10-len(details[1]))}|{details[2] + ' '*(12-len(details[2]))}|{details[3] + ' '*(15-len(details[3]))}|{details[4] + ' '*(15-len(details[4]))}|{details[5] + ' '*(12-len(details[5]))}|{details[6] + ' '*(10-len(details[6]))}|")
                        print("---------------------------------------------------------------------------------")
                        return
            else:
                print("Employee Not Found")


    def view_all_employees(self):
        is_empty = self.is_empty()
        if is_empty:
            print("No employee Records found in Database ")
        else:
            data = self.read_employees()
            print("---------------------------------------------------------------------------------")
            print(f"|Emp Name  |Role        |Job type       |Working Hours  |Salary / h  |Salary    |")
            print("---------------------------------------------------------------------------------")
            for line in data:
                details = line.strip().split(',')
                print(f"|{details[1] + ' '*(10-len(details[1]))}|{details[2] + ' '*(12-len(details[2]))}|{details[3] + ' '*(15-len(details[3]))}|{details[4] + ' '*(15-len(details[4]))}|{details[5] + ' '*(12-len(details[5]))}|{details[6] + ' '*(10-len(details[6]))}|")
            print("---------------------------------------------------------------------------------")            


class PayrollSystem(Admin):
    def is_empty(self):
        with open('payroll.txt','r') as f:
            data = f.readlines()
        if len(data) == 0:
            return True
        else:
            return False
            
    def read_payroll(self):
        with open('payroll.txt','r') as f:
            data = f.readlines()
        return data
        
    def check_payroll(self,emp_id):
        with open('payroll.txt','r') as f:
            data = f.readlines()

        is_found = False
        for line in data:
            details = line.strip().split(',')
            if emp_id == int(details[0]):
                is_found = True
        return is_found
        

    def calculate_salary(self):
        is_empty = self.is_empty()
        if is_empty:
            print("No employee Records found in Database ")
        else:
            emp_id = int(input("Enter Employee ID : "))
            emp_status = self.check_payroll(emp_id)
            if emp_status:
                data = self.read_payroll()
                for line in data:
                    details = line.strip().split(',')
                    if emp_id == int(details[0]):
                        break
                data = self.read_employees()
                for line in data:
                    details_2 = line.strip().split(',')
                    if emp_id == int(details_2[0]):
                        print("Employee ID   : ",details_2[0])
                        print("Employee Name : ",details_2[1])
                        print("Role          : ",details_2[2])
                        print("Job Type      : ",details_2[3])
                        print("Salary        : ",details[1])
                        print("Tax           : ",details[2])
                        print("Bonus         : ",details[3])
                        print("Final Salary  : ",details[4])
                        break
            else:
                print("Employee Not Found")


    def add_bonus(self):
        is_empty = self.is_empty()
        if is_empty:
            print("No employee Records found in Database ")
        else:
            emp_id = int(input("Enter Employee ID : "))
            emp_status = self.check_payroll(emp_id)
            if emp_status:
                bonus = int(input("Enter Bonus for the Employee : "))
                data = self.read_payroll()
                with open('payroll.txt','w') as f:
                    for line in data:
                        details = line.strip().split(',')
                        if emp_id == int(details[0]):
                            new_salary = (int(details[1]) - int(details[2])) + bonus
                            f.write(f"{details[0]},{details[1]},{details[2]},{bonus},{new_salary}\n")
                        else:
                            f.write(line)
                print("Bonus Added Successfully")
            else:
                print("Employee Not Found")


    def monthly_payroll(self):
        is_empty = self.is_empty()
        if is_empty:
            print("No employee Records found in Database ")
        else:
            data = self.read_payroll()
            total_salary = 0
            total_tax = 0
            total_bonus = 0
            final_salary = 0
            for line in data:
                details = line.strip().split(',')
                total_salary += int(details[1])
                total_tax += int(details[2])
                total_bonus += int(details[3])
                final_salary += int(details[4])
            print("----- Payroll of the Company -----\n")
            print("Total Salary of the employees :",total_salary)
            print("Total Tax                     :",total_tax)
            print("Total Bonus                   :",total_bonus)
            print("Final Salary to be paid to the employees :",final_salary)


    def payslip(self):
        is_empty = self.is_empty()
        if is_empty:
            print("No employee Records found in Database ")
        else:
            emp_id = int(input("Enter Employee ID :"))
            emp_status = self.check_payroll(emp_id)
            if emp_status:
                data = self.read_payroll()
                for line in data:
                    details = line.strip().split(',')
                    if emp_id == int(details[0]):
                        break

                data = self.read_employees()
                for line in data:
                    details_2 = line.strip().split(',')
                    if emp_id == int(details_2[0]):
                        print("----- Pay Slip of the Employee -----\n")
                        print("Name of the employee :",details_2[1])
                        print("Role                 :",details_2[2])
                        print("Job Type             :",details_2[3])
                        print("Salary               :",details[1])
                        print("Total Tax            :",details[2])
                        print("Bonus                :",details[3])
                        print("Final Salary         :",details[4])
                        print("------------------------------------")
            else:
                print("Employee not found")





admin = Admin()
payroll = PayrollSystem()
print("Welcome to Employee Payroll System !")
while True:
    print("\n----- MAIN MENU -----")
    print("1. Employee Management")
    print("2. Payroll")
    print("3. Payslip")
    print("4. Exit")
    choice = int(input("Enter your choice : "))
    match choice:
        case 1:
            while True:
                print("\n----- Employee Management -----")
                print("1. Add Employee")
                print("2. Remove Employee")
                print("3. View Employee")
                print("4. View All EMployees")
                print("5. Go Back To MAIN MENU")
                choice = int(input("Enter your choice : \n"))
                match choice:
                    case 1:
                        admin.add_employee()
                    case 2:
                        admin.remove_employee()
                    case 3:
                        admin.view_employee()
                    case 4:
                        admin.view_all_employees()
                    case 5:
                        break
        case 2:
            while True:
                print("\n----- Payroll System -----")
                print("1. Calculate Salary")
                print("2. Add Bonus")
                print("3. Monthly Payroll")
                print("4. Go Back To MAIN MENU")
                choice = int(input("Enter your choice : \n"))
                match choice:
                    case 1:
                        payroll.calculate_salary()
                    case 2:
                        payroll.add_bonus()
                    case 3:
                        payroll.monthly_payroll()
                    case 4:
                        break
        case 3:
            payroll.payslip()

        case 4:
            print("Application Closed Successfully !\n")
            break