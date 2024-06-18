from django.db import models

class Client(models.Model):
    account_number = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    inn = models.CharField(max_length=100)
    responsible_person = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='Not Working')

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.middle_name}'

class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
