# Generated by Django 5.0.6 on 2024-08-04 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='description',
        ),
    ]
