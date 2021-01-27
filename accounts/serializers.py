from .models import User, Department
from calendars.models import Calendar
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    calendars = serializers.PrimaryKeyRelatedField(many=True, queryset=Calendar.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'patronymic', 'department_id', 'specialization', 'calendars', 'events']

        def update(self, instance, validated_data):
            profile_data = validated_data.pop('userprofile', {})

            instance = super(UserSerializer, self).update(instance, validated_data)

            # get and update user profile
            profile = instance.userprofile
            if profile_data:
                profile.save()
            return instance
