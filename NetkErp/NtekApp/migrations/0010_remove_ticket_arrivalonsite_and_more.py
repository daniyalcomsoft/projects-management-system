# Generated by Django 4.1.1 on 2022-10-31 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NtekApp', '0009_alter_ticket_parentticketno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ArrivalOnSite',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='CurrentTicketStatus',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='FEAssigned',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='KmEnd',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='KmStart',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='KmTillSite',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='LeaveSite',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ParentTicketNo',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='RepairStart',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='RepairStop',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ScopeOfWork',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='SiteAddress',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TicketCreateDate',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TicketNo',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TicketSubType',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TravelStart',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='TravelStop',
        ),
        migrations.AddField(
            model_name='ticket',
            name='Billable',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='NtekApp.billable'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='ReferenceNo',
            field=models.CharField(default=1, max_length=255, verbose_name='Reference No'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='Subject',
            field=models.TextField(verbose_name='Subject'),
        ),
    ]
