from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calendars import views

router = DefaultRouter()
router.register(r'calendars', views.CalendarViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls))
]
