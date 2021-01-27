from rest_framework.decorators import api_view

from calendars.permissions import IsOwnerOrStaff
from rest_framework import viewsets, permissions
from calendars.models import Calendar, Event
from calendars.serializers import CalendarSerializer, EventSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrStaff]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrStaff]
    def get_queryset(self):
        user = self.request.user
        if not self.request.user.is_staff:
            return Event.objects.filter(owner=user)
        else:
            return Event.objects.all()

    @api_view(["DELETE"])
    def product_delete_rest_endpoint(request, id):
        Event.objects.get(event_id=id).delete()

