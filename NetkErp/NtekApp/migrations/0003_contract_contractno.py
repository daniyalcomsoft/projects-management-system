# Generated by Django 4.1.1 on 2022-10-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0002_remove_project_projectsubtype_project_endclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='ContractNo',
            field=models.CharField(default=1, max_length=255, verbose_name='Contract No'),
            preserve_default=False,
        ),
    ]