# Generated by Django 4.1 on 2023-08-12 09:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0011_alter_student_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="image",
        ),
    ]
