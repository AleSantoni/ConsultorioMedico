# Generated by Django 5.0 on 2024-03-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_alter_paciente_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='observaciones',
            field=models.TextField(),
        ),
    ]