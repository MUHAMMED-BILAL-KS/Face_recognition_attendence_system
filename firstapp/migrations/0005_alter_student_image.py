# Generated by Django 4.1 on 2023-08-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0004_student_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="image",
            field=models.ImageField(default=None, upload_to=""),
        ),
    ]
