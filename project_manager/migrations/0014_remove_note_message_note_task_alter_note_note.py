# Generated by Django 4.2.10 on 2024-02-29 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("project_manager", "0013_alter_profile_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="message",
        ),
        migrations.AddField(
            model_name="note",
            name="task",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_note",
                to="project_manager.task",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="note",
            name="note",
            field=models.TextField(),
        ),
    ]
