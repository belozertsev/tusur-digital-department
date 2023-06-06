# Generated by Django 4.2.1 on 2023-06-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("username", models.CharField(max_length=30)),
                ("creator", models.CharField(max_length=30)),
                ("header", models.CharField(max_length=50)),
                ("text", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "username",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Right",
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
                ("username", models.CharField(max_length=30)),
                ("applicant", models.CharField(max_length=30)),
                ("get_right", models.BooleanField()),
                ("post_right", models.BooleanField()),
                ("put_right", models.BooleanField()),
                ("delete_right", models.BooleanField()),
            ],
            options={
                "unique_together": {("username", "applicant")},
            },
        ),
    ]