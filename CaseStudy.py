class TimeSheet:
    def __init__(self):
        self.hours=int(input("Enter Hours Spent : "))
        self.activity=input("Enter Activity : ")
        self.date=input("Enter date in dd/mm/yyyy format : ")
class Employee(TimeSheet):
    def __init__(self):
        self.Name=input("Enter Employee Name : ")
        self.EmpId=int(input("Enter Employee ID : " ))
        self.Age=int(input("Enter Your Age : "))
        self.Email=input("Enter Your Email : ")
        self.Mobile=input("Enter Your Mobile Number : ")
        self.Address=input("Enter Your Address : ")
        s=input("Add Time Sheet Y/N : ")
        if s in ('y', 'Y'):
            super().__init__()
s=input("""Add employee details type E
Add Time sheet for existing employee type T :""")
if s in ('e','E'):
    e=Employee()
    print(e.__dict__)
elif s in ('t','T'):
    t=TimeSheet()
else:
    print("Invalid")
    