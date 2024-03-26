# Generated by Django 5.0.3 on 2024-03-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nome", models.CharField(max_length=100)),
                ("endereco", models.TextField()),
                ("cpf", models.CharField(max_length=14, unique=True)),
                ("data_nascimento", models.DateField()),
            ],
        ),
    ]