# Generated by Django 3.1.4 on 2020-12-10 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendars', '0005_auto_20201210_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='calendars', to='accounts.user'),
            preserve_default=False,
        ),
    ]
