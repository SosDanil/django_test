# Generated by Django 5.0.3 on 2024-04-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_alter_dog_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='дата рождения'),
        ),
    ]
