# Generated by Django 5.0.1 on 2024-01-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Voting", "0009_rename_candidate_name_votes_candidate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="photo",
            field=models.ImageField(
                blank=True, default="deault-avatar.png", null=True, upload_to="users/"
            ),
        ),
    ]
