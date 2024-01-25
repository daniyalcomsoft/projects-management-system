# Generated by Django 4.1.1 on 2022-11-06 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0036_fework'),
    ]

    operations = [
        migrations.AddField(
            model_name='fework',
            name='FEngg',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='NtekApp.fieldengineer', verbose_name='Field Engineer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fework',
            name='Ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='NtekApp.ticket', verbose_name='Ticket'),
            preserve_default=False,
        ),
    ]
