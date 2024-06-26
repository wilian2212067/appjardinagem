# Generated by Django 5.0.6 on 2024-05-12 23:35

import django.db.models.deletion
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
                ("endereco", models.CharField(max_length=255)),
                ("telefone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Servico",
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
                ("data", models.DateField()),
                ("hora", models.TimeField()),
                ("tipo_servico", models.CharField(max_length=100)),
                (
                    "fotos",
                    models.ImageField(
                        blank=True, null=True, upload_to="servico_fotos/"
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.cliente"
                    ),
                ),
            ],
        ),
    ]
