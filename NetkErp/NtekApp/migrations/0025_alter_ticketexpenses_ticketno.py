# Generated by Django 4.1.1 on 2022-11-04 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0024_remove_tickeadminstatus_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketexpenses',
            name='TicketNo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='NtekApp.ticket', verbose_name='Ticket No'),
        ),
    ]