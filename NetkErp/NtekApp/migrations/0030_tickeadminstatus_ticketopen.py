# Generated by Django 4.1.1 on 2022-11-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0029_remove_tickeadminstatus_ticketopen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickeadminstatus',
            name='TicketOpen',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ticket Open'),
        ),
    ]
