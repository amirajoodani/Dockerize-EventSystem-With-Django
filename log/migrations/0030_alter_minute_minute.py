# Generated by Django 3.2.12 on 2022-07-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0029_alter_minute_minute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minute',
            name='minute',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
