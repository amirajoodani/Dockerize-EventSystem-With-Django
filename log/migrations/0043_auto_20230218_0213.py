# Generated by Django 3.2 on 2023-02-17 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0042_auto_20230101_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='year_of_start',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auth.user+', to='log.year'),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='year_of_start',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='log.year'),
        ),
    ]
