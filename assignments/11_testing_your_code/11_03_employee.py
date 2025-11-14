class Employee:

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        self.annual_salary += amount


from employee import Employee

def test_give_default_raise():
    em = Employee('Easton', 'Sherwood', 50000)
    em.get_raise()
    assert em.annual_salary == 55000

def test_give_custom_raise():
    em = Employee('Pat','Cruz', 60000)
    em.give_raise(15000)
    assert em.annual_salary == 75000


import pytest
from employee import Employee

def default_employee():
    return Employee('Easton','Sherwood', 55000)

def custom_employee():
    return Employee('Pat','Cruz', 60000)

def test_give_default_raise(default_employee):
    default_employee.give_raise()
    assert default_employee.annual_salary == 55000

def test_give_custom_raise(custom_raise):
    custom_employee.give_raise(15000)
    assert custom_employee.annual_salary == 75000