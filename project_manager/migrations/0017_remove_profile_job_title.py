# Generated by Django 4.2.10 on 2024-03-04 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project_manager", "0016_remove_profile_title_profile_job_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="job_title",
        ),
    ]
