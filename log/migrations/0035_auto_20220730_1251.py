# Generated by Django 3.2.12 on 2022-07-30 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0034_alter_minute_minute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='export_to_csv',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='export_to_csv',
        ),
    ]