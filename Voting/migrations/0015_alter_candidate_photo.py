# Generated by Django 5.0.1 on 2024-01-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Voting", "0014_alter_candidate_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="photo",
            field=models.ImageField(blank=True, upload_to="media"),
        ),
    ]
