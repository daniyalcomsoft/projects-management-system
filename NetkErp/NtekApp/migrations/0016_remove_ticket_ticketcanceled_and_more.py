# Generated by Django 4.1.1 on 2022-11-01 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0015_ticket_descp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='TicketCanceled',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TicketClosed',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TicketOnHold',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TicketSchedule',
        ),
    ]
