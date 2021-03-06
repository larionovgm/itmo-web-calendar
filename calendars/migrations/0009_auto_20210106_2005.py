# Generated by Django 3.1.4 on 2021-01-06 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendars', '0008_auto_20201211_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='calendar_id',
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='type_of_duty',
            field=models.IntegerField(blank=True, choices=[(1, 'First'), (2, 'Second'), (3, 'Third')], null=True),
        ),
    ]
