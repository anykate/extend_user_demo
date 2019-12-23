from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        employee, created = Employee.objects.get_or_create(user=instance)

post_save.connect(create_employee, sender=User)
