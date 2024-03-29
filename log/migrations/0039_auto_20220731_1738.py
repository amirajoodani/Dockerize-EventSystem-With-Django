# Generated by Django 3.2.12 on 2022-07-31 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0038_auto_20220731_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventkindofproblem',
            name='hour_of_end2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='eventkindofproblem',
            name='hour_of_start2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='eventkindofproblem',
            name='minute_of_end2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='eventkindofproblem',
            name='minute_of_start2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AddField(
            model_name='eventkindofproblem',
            name='mounth_of_end2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='eventkindofproblem',
            name='mounth_of_start2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='eventkindofproblem',
            name='year_of_end2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
        migrations.AddField(
            model_name='eventkindofproblem',
            name='year_of_start2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='hour_of_end2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='hour_of_start2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='minute_of_end2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='minute_of_start2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='mounth_of_end2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='mounth_of_start2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='year_of_end2',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='year_of_start2',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
    ]
