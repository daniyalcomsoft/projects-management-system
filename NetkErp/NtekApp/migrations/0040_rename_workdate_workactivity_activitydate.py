# Generated by Django 4.1.1 on 2022-11-06 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0039_alter_workactivity_workdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workactivity',
            old_name='WorkDate',
            new_name='ActivityDate',
        ),
    ]