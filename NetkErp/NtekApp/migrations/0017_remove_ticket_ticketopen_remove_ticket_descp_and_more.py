# Generated by Django 4.1.1 on 2022-11-01 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0016_remove_ticket_ticketcanceled_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='TicketOpen',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='descp',
        ),
        migrations.CreateModel(
            name='TickeAdminStatus',
            fields=[
                ('TASID', models.AutoField(primary_key=True, serialize=False)),
                ('TicketOpen', models.BooleanField(default=True, verbose_name='Ticket Open')),
                ('TicketSchedule', models.BooleanField(default=False, verbose_name='Ticket Schedule')),
                ('TicketClosed', models.BooleanField(default=False, verbose_name='Ticket Closed')),
                ('TicketOnHold', models.BooleanField(default=False, verbose_name='Ticket On Hold')),
                ('TicketCanceled', models.BooleanField(default=False, verbose_name='Ticket Cancel')),
                ('Description', models.TextField(verbose_name='Description')),
                ('Ticket', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='NtekApp.ticket', verbose_name='Ticket No')),
            ],
        ),
    ]