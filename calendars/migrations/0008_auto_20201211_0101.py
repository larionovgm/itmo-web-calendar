# Generated by Django 3.1.4 on 2020-12-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0007_auto_20201211_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.CharField(blank=True, max_length=1023, verbose_name='Notes'),
        ),
    ]