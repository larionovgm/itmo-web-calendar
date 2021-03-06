# Generated by Django 3.1.4 on 2020-12-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department_id',
            field=models.ManyToManyField(blank=True, to='accounts.Department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='specialization',
            field=models.CharField(blank=True, choices=[('PS', 'Pediatric Surgeon'), ('S', 'Surgeon'), ('PA', 'Pediatric Anesthesiologist'), ('A', 'Anesthesiologist')], max_length=2, null=True),
        ),
    ]
