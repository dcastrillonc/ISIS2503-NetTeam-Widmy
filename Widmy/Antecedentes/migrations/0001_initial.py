# Generated by Django 3.2.6 on 2023-03-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id_antecedente', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion_antecedente', models.CharField(max_length=2000)),
            ],
        ),
    ]
