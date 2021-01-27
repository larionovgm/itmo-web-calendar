from django.db import models
from django.conf import settings
DutyType = models.IntegerChoices('DutyType', 'FIRST SECOND THIRD')
# Create your models here.
class Calendar(models.Model):
  calendar_name = models.CharField('Calendar name', max_length=255)
  calendar_id = models.AutoField(primary_key=True)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='calendars',on_delete=models.CASCADE)

class Event(models.Model):
  class EventType(models.TextChoices):
     DUTY = 'D'
     SICK_LEAVE = 'S'
     VACATION = 'V'
  event_id = models.AutoField(primary_key=True)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='events', on_delete=models.CASCADE)
  title = models.CharField('Title', max_length=255)
  start = models.DateTimeField('Start time')
  end = models.DateTimeField('End time')
  allDay = models.BooleanField('All day event', default= True)
  type_of_event = models.CharField(choices=EventType.choices, max_length=2)
  type_of_duty = models.IntegerField(choices=DutyType.choices, blank=True, null=True)
  notes = models.CharField('Notes', max_length=1023, blank=True)