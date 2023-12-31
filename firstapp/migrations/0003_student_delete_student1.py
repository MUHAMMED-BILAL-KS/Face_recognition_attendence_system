# Generated by Django 4.1 on 2023-08-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firstapp", "0002_student1_delete_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=70)),
                ("last_name", models.CharField(max_length=70)),
                ("phone", models.BigIntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("dob", models.DateField()),
                ("clas", models.CharField(max_length=50, verbose_name="class")),
                ("rollno", models.IntegerField()),
                ("collage", models.CharField(max_length=50)),
                ("district", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name="student1",
        ),
    ]
