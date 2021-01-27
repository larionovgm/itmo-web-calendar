# Generated by Django 3.1.4 on 2020-12-11 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0006_calendar_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='calendar_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='calendars.calendar'),
        ),
    ]
