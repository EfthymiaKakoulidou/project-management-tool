# Generated by Django 4.2.10 on 2024-03-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project_manager", "0022_alter_task_assigned_to"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="last_name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
