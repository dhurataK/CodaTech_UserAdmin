from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
import re

# Create your models here.
class ClientManager(models.Manager):
    def create_user(self, data, admin):
        errors = []
        if len(data['first_name']) < 2:
            errors.append('Please enter a valid first name')
        if bool(re.search(r'\d', data['first_name'])):
            errors.append('Please enter a valid first name')
        if len(data['last_name']) < 2:
            errors.append('Please enter a valid last name')
        if bool(re.search(r'\d', data['last_name'])):
            errors.append('Please enter a valid last name')
        if len(data['iban']) < 2:
            errors.append('Please enter a valid IBAN')

        if not errors:
            new_client = self.create(first_name=data['first_name'], last_name=data['last_name'], iban=data['iban'], admin=admin)
            return (True, new_client)
        else:
            print('Tek errorat te modeli')
            return (False, errors)

class Client(models.Model):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    iban = models.CharField(max_length=45, blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ClientManager()

    class Meta:
        db_table = 'tb_clients'
