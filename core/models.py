from django.db import models
from django.db.models import CASCADE, Sum


class Position(models.Model):
    LEVEL_CHOICES = (
        ('TR', 'Trainee '),
        ('JR', 'Junior'),
        ('MD', 'Middle'),
        ('MP', 'MiddlePlus'),
        ('SR', 'Senior'),
    )
    position = models.CharField(max_length=30, verbose_name='Должность')
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='TR')

    def __str__(self):
        return f'{self.position} {self.level}'


class Employee(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    position = models.ForeignKey(Position, on_delete=CASCADE, verbose_name='Должность')
    employment_date = models.DateField(auto_now=True, verbose_name='Дата приема на работу')
    chief = models.ForeignKey('self', on_delete=CASCADE, verbose_name='Ссылка на объект начальника.', null=True,
                              blank=True)
    wages = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')

    @property
    def get_all_salary(self):
        all_salary = self.salary_set.aggregate(Sum('sum_paid'))
        return all_salary.get('sum_paid__sum', 0)

    def salary(self):
        return self.salary_set.all()

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=CASCADE, verbose_name='Работник')
    date_paid = models.DateField(verbose_name='Дата перечисления')
    sum_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')

    def __str__(self):
        return f'{self.sum_paid} {self.date_paid} {self.employee}'






