# Generated by Django 5.0.1 on 2024-01-22 15:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Voting", "0005_alter_vote_vote_no"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vote",
            old_name="vote_no",
            new_name="votes",
        ),
    ]