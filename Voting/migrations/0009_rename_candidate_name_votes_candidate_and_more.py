# Generated by Django 5.0.1 on 2024-01-23 11:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Voting", "0008_remove_votes_vote"),
    ]

    operations = [
        migrations.RenameField(
            model_name="votes",
            old_name="candidate_name",
            new_name="candidate",
        ),
        migrations.RenameField(
            model_name="votes",
            old_name="user_name",
            new_name="user",
        ),
    ]
