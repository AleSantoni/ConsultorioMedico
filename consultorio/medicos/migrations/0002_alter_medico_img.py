# Generated by Django 5.0 on 2024-03-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='doctor'),
        ),
    ]
