import datetime

class Employee:
    num_of_emps = 0
    def __init__(self , first , last , pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.emil = first + '.' + last + '@email.com'
        Employee.num_of_emps += 1
    def full_name(self):
        return '{} {}'.format(first , last)
    def apply_raise(self):
        self.pay = self.pay * raise_amt
    @classmethod
    def set_raise_amt(cls , amount):
        cls.raise_amt = amount
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('mostafa','saleh',50000)
emp2 = Employee('mohamed','afifi',70000)

my_date = datetime.date(2018,9,3)
print(Employee.is_workday(my_date))

