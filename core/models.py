from django.db import models
import uuid

class Manager(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='employees')

    def __str__(self):
        return self.name
