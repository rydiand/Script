class Employee:
    num_of_empl = 0
    def __init__(self, first, last, phone):

         self.first = first
         self.last = last
         self.phone = phone
         self.email = first + '.' + last + '@nordea.com'
         Employee.num_of_empl += 1

    def __repr__(self):
         return 'Name: {} {} - Phone: {}'.format(self.first, self.last, self.phone)

    def __str__(self):
         return 'Name: {} {} - Phone: {} - E-mail:: {}'.format(self.first, self.last, self.phone, self.email)

    def getFullname(self):
         return '{} {}'.format(self.first, self.last)

    @classmethod
    def getNumber(cls):
         return cls.num_of_empl

    @staticmethod
    def is_workday(day):
         if day.weekday() == 5 or day.weekday() == 6:
             return "Day off."
         return "Workday."

class Developer(Employee):
    pass

class Manager(Employee):
    pass

emp_1 = Employee('Torben', 'Rydiander', '+45 2529 2306')
emp_2 = Employee('Jan', 'Vinten', '+45 1234 5678')
emp_3 = Employee('Per', 'Trangbæk', '+45 1234 5678')

mgr_1 = Manager('Robert', 'Piil', '+45 8765 4321')

print(mgr_1)
print(emp_3.getFullname())
print(Employee.getNumber())
print(emp_1)
print(emp_1.__repr__())

import datetime
now = datetime.datetime.now()
today = datetime.date(now.year, now.month, now.day)
print(Employee.is_workday(today))

import sys
#print("\t".join(sys.argv[2]))

from datetime import date 
a = date(2017,11,2)
b = date(2017,6,29)
print ((a-b).days)
