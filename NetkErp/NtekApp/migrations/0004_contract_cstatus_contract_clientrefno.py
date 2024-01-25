# Generated by Django 4.1.1 on 2022-10-27 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0003_contract_contractno'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='CStatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='NtekApp.contractstatus', verbose_name='Contract Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='ClientRefNo',
            field=models.CharField(default=1, max_length=255, verbose_name='Client Ref No'),
            preserve_default=False,
        ),
    ]