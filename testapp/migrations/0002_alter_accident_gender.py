# Generated by Django 4.1.7 on 2023-03-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accident",
            name="gender",
            field=models.IntegerField(choices=[(0, "Male"), (1, "Female")]),
        ),
    ]
