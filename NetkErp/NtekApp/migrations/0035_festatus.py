# Generated by Django 4.1.1 on 2022-11-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0034_ticketagainstfe_email_ticketagainstfe_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FEStatus',
            fields=[
                ('FEID', models.AutoField(primary_key=True, serialize=False)),
                ('FEStatus', models.CharField(max_length=255, verbose_name='Field Engineer Status')),
            ],
        ),
    ]
