# Generated by Django 3.2.6 on 2023-03-17 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sede', models.CharField(max_length=50)),
                ('fecha', models.CharField(max_length=50)),
                ('hora', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('completada', models.BooleanField()),
            ],
        ),
    ]
