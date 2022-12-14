# Generated by Django 4.1.3 on 2022-11-19 17:00

from django.db import migrations, models
import django.db.models.deletion
import trials.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("summary", models.TextField()),
                ("description", models.TextField()),
                ("hidden", models.BooleanField(default=True)),
            ],
            bases=(models.Model, trials.models.TimeTracked),
        ),
        migrations.CreateModel(
            name="Stage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("summary", models.TextField()),
                ("description", models.TextField()),
                ("hidden", models.BooleanField(default=True)),
                (
                    "trial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trials.trial"
                    ),
                ),
            ],
            bases=(models.Model, trials.models.TimeTracked),
        ),
    ]
