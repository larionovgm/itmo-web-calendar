from django.test import TestCase
from calendars.models import Calendar, Event
from accounts.models import User
from datetime import datetime
# Create your tests here.

class CalendarTestCase(TestCase):
  def setUp(self):
    test_user = User.objects.create(username='tester')
    test_calendar = Calendar.objects.create(calendar_name='test',
                                            owner=test_user)
    Event.objects.create(
      calendar_id=test_calendar,
      title='test_event',
      start=datetime(2020,9,30,23,55),
      end=datetime(2020, 9, 30, 23, 59),
      allDay=False,
      type_of_event='V',
    )

  def test_event_link(self):
    test_calendar = Calendar.objects.get(calendar_name='test')
    test_event = Event.objects.get(calendar_id=test_calendar)
    self.assertEqual(test_event.title, 'test_event')

  def test_user_link(self):
    test_user = User.objects.get(username='tester')
    test_calendar = Calendar.objects.get(owner=test_user)
    self.assertEqual(test_calendar.calendar_name, 'test')
