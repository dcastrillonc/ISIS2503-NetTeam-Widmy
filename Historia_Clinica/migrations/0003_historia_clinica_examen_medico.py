# Generated by Django 3.2.6 on 2023-04-11 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamenMedico', '0002_auto_20230411_1317'),
        ('Historia_Clinica', '0002_auto_20230318_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia_clinica',
            name='examen_Medico',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ExamenMedico.examenmedico'),
        ),
    ]