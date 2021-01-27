from rest_framework import serializers
from .models import Calendar, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_id', 'owner', 'title', 'start', 'end', 'allDay', 'type_of_event', 'type_of_duty', 'notes']


class CalendarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Calendar
        fields = ['calendar_name', 'calendar_id', 'owner']
