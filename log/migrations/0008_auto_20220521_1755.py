# Generated by Django 3.2.12 on 2022-05-21 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0007_alter_eventkindofproblem_status_of_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert11',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert12',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='Expert9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expert+', to='log.expert'),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]