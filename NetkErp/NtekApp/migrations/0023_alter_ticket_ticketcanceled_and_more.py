# Generated by Django 4.1.1 on 2022-11-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0022_alter_ticket_ticketopen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='TicketCanceled',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ticket Cancel'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='TicketClosed',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ticket Closed'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='TicketOnHold',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ticket On Hold'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='TicketOpen',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ticket Open'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='TicketSchedule',
            field=models.BooleanField(blank=True, null=True, verbose_name='Ticket Schedule'),
        ),
    ]