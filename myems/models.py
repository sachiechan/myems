from __future__ import unicode_literals

from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'employee'

class Department(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    class Meta:
        db_table = 'departments'


class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no')
    dept_no = models.ForeignKey(Department, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_emp'
        unique_together = (('emp_no', 'dept_no'),)


class DeptManager(models.Model):
    dept_no = models.ForeignKey(Department, db_column='dept_no')
    emp_no = models.ForeignKey(Employee, db_column='emp_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_manager'
        unique_together = (('emp_no', 'dept_no'),)


class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no', related_name='employeeSalaries')
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return 'Employee {} Salary {}',self.emp_no, self.salary

    class Meta:
        db_table = 'salaries'
        unique_together = (('emp_no', 'from_date'),)


class Titles(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no', related_name='employeeTitles')
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'titles'
