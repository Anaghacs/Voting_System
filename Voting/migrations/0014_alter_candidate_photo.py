# Generated by Django 5.0.1 on 2024-01-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Voting", "0013_alter_candidate_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="photo",
            field=models.ImageField(blank=True, default="Abc", upload_to="candidate"),
            preserve_default=False,
        ),
    ]
