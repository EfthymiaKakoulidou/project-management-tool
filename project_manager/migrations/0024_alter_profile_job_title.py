# Generated by Django 4.2.10 on 2024-03-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "project_manager",
            "0023_alter_profile_first_name_alter_profile_last_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="job_title",
            field=models.CharField(max_length=200),
        ),
    ]
