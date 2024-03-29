# Generated by Django 3.2 on 2023-02-17 22:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0044_alter_eventkindofproblem_year_of_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='year_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='year_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
    ]
