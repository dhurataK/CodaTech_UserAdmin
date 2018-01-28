from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
import re

# Create your models here.
class ClientManager(models.Manager):

    #Create a new client
    def create_client(self, data, admin):
        errors = self.validate_data(data)
        if len(errors)>0:
            return (False, errors)
        else:
            new_client = self.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                iban=data['iban'],
                admin=admin
            )
            return (True, new_client)

    #Updated client
    def update_client(self, data):
        errors = self.validate_data(data)
        if len(errors)>0:
            return (False, errors)
        else:
            updated_client = Client.objects.filter(id=int(data['id'])).update(first_name=data['first_name'], last_name=data['last_name'], iban=data['iban'])
            return (True, data['id'])
            
    #Check data
    def validate_data(self, data):
        errors = []
        #validate data
        if len(data['first_name']) < 1:
            errors.append('The first name can not be blank')
        if bool(re.search(r'\d', data['first_name'])):
            errors.append('Please enter a valid first name')
        if len(data['last_name']) < 1:
            errors.append('The last name can not be blank')
        if bool(re.search(r'\d', data['last_name'])):
            errors.append('Please enter a valid last name')
        if len(data['iban']) < 1:
            errors.append('Please include a IBAN number')
        if not data['iban'].isdigit():
            errors.append('Please include a valid IBAN number')

        return errors

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
