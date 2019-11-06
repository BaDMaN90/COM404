# Python object-oriantaited Programming


class Employee:

    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps +=1

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Luis", "Smith", 50000)
emp_2 = Employee("Ricky", "Vega", 40000)
boss_1 = Employee("Fill", "Sanchez", 95000)

import datetime
my_date = datetime.date(2019, 11, 9)
print(Employee.is_workday(my_date))

#emp_str_1 = "John-Doe-65000"
#emp_str_2 = "Steve-Hill-35000"
#emp_str_3 = "Jane-Doe-45000"

#first, last, pay = emp_str_1.split("-")

#new_emp_1 = Employee.from_string(emp_str_1)
#new_emp_2 = Employee.from_string(emp_str_2)

#print(new_emp_1.email)
#print(new_emp_1.pay)
#print(new_emp_2.email)
#print(new_emp_2.pay)

#print(boss_1.raise_amount)
#Employee.set_raise_amount(1.06)
#print(Employee.raise_amount)




#print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
#print(emp_2.fullname())

#print(Employee.fullname(emp_1))
# print(Employee.fullname(emp_2))

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#print(emp_1.__dict__)
#print(Employee.__dict__)

#print(Employee.num_of_emps)