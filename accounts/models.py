from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class User(AbstractUser):
    class Specialization(models.TextChoices):
      PEDIATRIC_SURGEON = 'PS'
      SURGEON = 'S'
      PEDIATRIC_ANESTHESIOLOGIST = 'PA'
      ANESTHESIOLOGIST = 'A'

    patronymic = models.CharField(max_length=50, null=True, blank=True)
    department_id = models.ManyToManyField("Department", blank=True)
    specialization = models.CharField(choices=Specialization.choices, null=True, max_length=2, blank=True)
    USERNAME_FIELD = 'username'
    pass

class Department(models.Model):
  department_id = models.AutoField(primary_key=True)
  head_of_department = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=True)
  department_name = models.CharField(max_length=255)