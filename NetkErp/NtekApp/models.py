from operator import truediv
from pyexpat import model
from random import choices
from tabnanny import verbose
from xmlrpc.client import boolean
from django.db import models
from email.policy import default
from ftplib import MAXLINE
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT')
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Country(models.Model):
    CountryID = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length=125, verbose_name="Country Name")

    def __str__(self):
        return self.CountryName

class City(models.Model):
    CityID = models.AutoField(primary_key=True)
    CityName = models.CharField(max_length=125, verbose_name='City Name')
    Country = models.ForeignKey(Country, verbose_name='Country Name', on_delete=models.CASCADE)

    def __str__(self):
        return self.CityName

class Client(models.Model):
    ClientID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255, verbose_name="Company Name")
    Address1 = models.CharField(max_length=500, verbose_name="Address1")
    Address2 = models.CharField(max_length=500, verbose_name="Address2")
    Country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.DO_NOTHING)
    City = models.ForeignKey(City, verbose_name="City", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.CompanyName

class EndClient(models.Model):
    EndClientID = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, verbose_name='Client', on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=255, verbose_name="Company Name")
    Address1 = models.CharField(max_length=500, verbose_name="Address1")
    Address2 = models.CharField(max_length=500, verbose_name="Address2")
    Country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.DO_NOTHING)
    City = models.ForeignKey(City, verbose_name="City", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.CompanyName

class ContractStatus(models.Model):
    CSID = models.AutoField(primary_key=True)
    ContractStatus = models.CharField(max_length=500, verbose_name="Contract Status")

    def __str__(self):
        return str(self.ContractStatus)

class ContractSLA(models.Model):
    SLAID = models.AutoField(primary_key=True)
    ContractSLA = models.CharField(max_length=500, verbose_name="Contract SLA")

    def __str__(self):
        return str(self.ContractSLA)

class ContractType(models.Model):
    CTID = models.AutoField(primary_key=True)
    ContractType = models.CharField(max_length=500, verbose_name="Contract Type")

    def __str__(self):
        return str(self.ContractType)

class ContractSubType(models.Model):
    CSTID = models.AutoField(primary_key=True)
    ContratctType = models.ForeignKey(ContractType, verbose_name="Contract Sub Type", on_delete=models.DO_NOTHING)
    ContractSubType = models.CharField(max_length=500, verbose_name="Contract Sub Type")

    def __str__(self):
        return str(self.ContractSubType)

class Contract(models.Model):
    ContractID = models.AutoField(primary_key=True)
    ContractNo = models.CharField(max_length=255, verbose_name='Contract No')
    ContractName = models.CharField(max_length=500, verbose_name="Contract Name")
    ClientRefNo = models.CharField(max_length=255, verbose_name="Client Ref No")
    Description = models.TextField()
    Client = models.ForeignKey(Client, verbose_name="Client", on_delete=models.DO_NOTHING)
    EndClient = models.ForeignKey(EndClient, verbose_name="End Client", on_delete=models.DO_NOTHING)
    StartDate = models.DateTimeField(auto_now_add=False, verbose_name="Start Date", blank=True, null=True)
    EndDate = models.DateTimeField(auto_now_add=False, verbose_name="End Date", blank=True, null=True)
    ContractType = models.ForeignKey(ContractType, verbose_name="Contract Type", on_delete=models.DO_NOTHING)
    # ContractSubType = models.ForeignKey(ContractSubType, verbose_name="Contract Sub Type", on_delete=models.DO_NOTHING)
    ContractSLA = models.ForeignKey(ContractSLA, verbose_name="Contract SLA", on_delete=models.DO_NOTHING)
    CStatus = models.ForeignKey(ContractStatus, verbose_name="Contract Status", on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.ContractName)

class ProjectStatus(models.Model):
    PSID = models.AutoField(primary_key=True)
    ProjectStatus = models.CharField(max_length=255, verbose_name="Project Status")

    def __str__(self):
        return str(self.ProjectStatus)

class ProjectType(models.Model):
    PTID = models.AutoField(primary_key=True)
    ProjectType = models.CharField(max_length=255, verbose_name="Project Type")

    def __str__(self):
        return str(self.ProjectType)

class ProjectSubType(models.Model):
    PSTID = models.AutoField(primary_key=True)
    ProjectType = models.ForeignKey(ProjectType, verbose_name="Project Type", on_delete=models.DO_NOTHING)
    ProjectSubType = models.CharField(max_length=500, verbose_name="Project Sub Type")

    def __str__(self):
        return str(self.ProjectSubType)    

class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=500, verbose_name='Project Name')
    ClientRefNo = models.CharField(max_length=255, verbose_name='Client Ref No')
    Description = models.TextField()
    Client = models.ForeignKey(Client, verbose_name="Client", on_delete=models.DO_NOTHING)
    StartDate = models.DateTimeField(auto_now_add=False, verbose_name="Start Date")
    EndDate = models.DateTimeField(auto_now_add=False, verbose_name="End Date")
    ProjectType = models.ForeignKey(ProjectType, verbose_name="Project Type", on_delete=models.DO_NOTHING)
    ProjectStauts = models.ForeignKey(ProjectStatus, verbose_name='Project Status', on_delete=models.DO_NOTHING)
    EndClient = models.ForeignKey(EndClient, verbose_name="End Client", on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.ProjectName)

class FieldEngineer(models.Model):
    FEID = models.AutoField(primary_key=True)
    EmployeeID = models.CharField(max_length=255, verbose_name='Employee ID')
    FirstName = models.CharField(max_length=255, verbose_name=("First Name"))
    LastName = models.CharField(max_length=255, verbose_name=("Last Name"))
    Country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.DO_NOTHING)
    City = models.ForeignKey(City, verbose_name="City", on_delete=models.DO_NOTHING)
    Email = models.CharField(max_length=255, verbose_name=("Email"))
    Mobile = models.CharField(max_length=255, verbose_name=("Mobile"))

    def __str__(self):
        return str(self.FirstName + ' ' + self.LastName)

class TicketStatus(models.Model):
    TSID = models.AutoField(primary_key=True)
    TicketStatus = models.CharField(max_length=255, verbose_name="Ticekt Status")

    def __str__(self):
        return str(self.TicketStatus)

class TicketStatusHistory(models.Model):
    TSHID = models.AutoField(primary_key=True)
    HistoryDate = models.DateTimeField(auto_now_add=False, verbose_name="History Date")
    Status = models.ForeignKey(TicketStatus, verbose_name="Status", on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return str(self.HistoryDate + '' + self.Status)

class TicketType(models.Model):
    TTID = models.AutoField(primary_key=True)
    TicketType = models.CharField(max_length=255, verbose_name="Ticket Type")

    def __str__(self):
        return str(self.TicketType)

class TicketSubType(models.Model):
    TSTID = models.AutoField(primary_key=True)
    TicketType = models.ForeignKey(TicketType, verbose_name="Ticket Type", on_delete=models.DO_NOTHING)
    TicketSubType = models.CharField(max_length=255, verbose_name="Ticket Sub Type")

    def __str__(self):
        return str(self.TicketSubType)

class BillAble(models.Model):
    BAID = models.AutoField(primary_key=True)
    Billable = models.CharField(max_length=255, verbose_name='Bill Able')

    def __str__(self):
        return self.Billable

class Ticket(models.Model):
    TID = models.AutoField(primary_key=True)
    Contract = models.ForeignKey(Contract, verbose_name="Contract", blank=True, null=True, on_delete=models.DO_NOTHING)
    Project = models.ForeignKey(Project, verbose_name="Project",blank=True, null=True, on_delete=models.DO_NOTHING)
    TicketType = models.ForeignKey(TicketType, verbose_name="Ticket Type", on_delete=models.DO_NOTHING)
    Billable = models.ForeignKey(BillAble, on_delete=models.DO_NOTHING)
    TicketScheduleDate = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name="Ticket Schedule Date")
    TicketCompletedDate = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name="Ticket Completed Date")
    Subject = models.TextField(verbose_name="Subject")
    Client = models.ForeignKey(Client, verbose_name="Client", on_delete=models.DO_NOTHING)
    EndClient = models.ForeignKey(EndClient, verbose_name="End Client", on_delete=models.DO_NOTHING)
    ReferenceNo = models.CharField(max_length=255, verbose_name='Reference No')    
    Country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.DO_NOTHING)
    City = models.ForeignKey(City, verbose_name="City", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.Subject
        
class TickeAdminStatus(models.Model):
    TASID = models.AutoField(primary_key=True)
    Ticket = models.ForeignKey(Ticket, verbose_name='Ticket', on_delete=models.DO_NOTHING)
    TicketStatus = models.ForeignKey(TicketStatus, verbose_name='Ticket Status', on_delete=models.DO_NOTHING)
    StatusDate = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name='Status Date')
    Description = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.Description

class TicketAgainstFE(models.Model):
    TAFEID = models.AutoField(primary_key=True)
    Ticket = models.ForeignKey(Ticket, verbose_name='Ticket No', on_delete=models.DO_NOTHING)
    FEngineer = models.ForeignKey(FieldEngineer, verbose_name='Field Engineer', on_delete=models.DO_NOTHING)
    Email = models.CharField(max_length=255, verbose_name='Email', blank=True, null=True)
    Mobile = models.CharField(max_length=255, verbose_name='Mobile', blank=True, null=True)
    Description = models.TextField(verbose_name='Description', blank=True, null=True)

    def __str__(self):
        return self.Description

class FEStatus(models.Model):
    FEID = models.AutoField(primary_key=True)
    FEStatus = models.CharField(max_length=255, verbose_name='Field Engineer Status')

    def __str__(self):
        return self.FEStatus

class FEWork(models.Model):
    FEWID = models.AutoField(primary_key=True)
    Ticket = models.ForeignKey(Ticket, verbose_name='Ticket', on_delete=models.DO_NOTHING)
    FEngg = models.ForeignKey(FieldEngineer, verbose_name='Field Engineer', on_delete=models.DO_NOTHING)
    FStatus = models.ForeignKey(FEStatus, verbose_name='Field Engineer Status', on_delete=models.DO_NOTHING)
    WorkDate = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name='Work Date')
    Kilometer = models.CharField(max_length=255, verbose_name='Kilometer', blank=True, null=True)

    def __str__(self):
        return self.Kilometer 

class WorkActivity(models.Model):
    WAID = models.AutoField(primary_key=True)
    Ticket = models.ForeignKey(Ticket, verbose_name='Ticket No', on_delete=models.DO_NOTHING)
    FEngg = models.ForeignKey(FieldEngineer, verbose_name='Field Engineer', on_delete=models.DO_NOTHING)
    RemoteClient = models.ForeignKey(Client, verbose_name='Remote Client', on_delete=models.DO_NOTHING)
    ActivityDate = models.DateTimeField(auto_now_add=False, blank=True, null=True, verbose_name='Activity Date')
    Description = models.TextField(verbose_name='Description', blank=True, null=True)

    def __str__(self):
        return self.Description
    
    


class TicketExpenses(models.Model):
    TEID = models.AutoField(primary_key=True)
    TicketNo = models.ForeignKey(Ticket, verbose_name="Ticket No", blank=True, null=True, on_delete=models.DO_NOTHING)
    FieldEngineer = models.ForeignKey(FieldEngineer, verbose_name="Field Engineer", on_delete=models.DO_NOTHING)
    ExpenseDate = models.DateTimeField(auto_now_add=False, verbose_name="Expense Date")
    Currency = models.CharField(max_length=255, verbose_name="Currency")
    Amount = models.DecimalField(max_length=None, verbose_name="Amount", decimal_places=2, max_digits=255)
    ExpenseReason = models.TextField(verbose_name="Expense Reason")

    def __str__(self) -> str:
        return str(self.TicketNo)

class TicketExternalNotes(models.Model):
    TENID = models.AutoField(primary_key=True)
    TicketNo = models.ForeignKey(Ticket, verbose_name="Ticket No", on_delete=models.DO_NOTHING)
    FieldEngineer = models.ForeignKey(FieldEngineer, verbose_name="Field Engineer", on_delete=models.DO_NOTHING)
    Date = models.DateTimeField(auto_now_add=False, verbose_name="Date")
    Notes = models.TextField(verbose_name="Notes")

    def __str__(self):
        return str(self.TENID)

class TicketInternalNotes(models.Model):
    TINID = models.AutoField(primary_key=True)
    TicketNo = models.ForeignKey(Ticket, verbose_name="Ticket No", on_delete=models.DO_NOTHING)
    FieldEngineer = models.ForeignKey(FieldEngineer, verbose_name="Field Engineer", on_delete=models.DO_NOTHING)
    Date = models.DateTimeField(auto_now_add=False, verbose_name="Date")
    Notes = models.TextField(verbose_name="Notes")

    def __str__(self):
        return str(self.TINID)

class TicketActionHistory(models.Model):
    TAHID = models.AutoField(primary_key=True)
    TicketNo = models.ForeignKey(Ticket, verbose_name="Ticket No", on_delete=models.DO_NOTHING)
    FieldEngineer = models.ForeignKey(FieldEngineer, verbose_name="Field Engineer", on_delete=models.DO_NOTHING)
    ActionTime = models.DateTimeField(auto_now_add=False, verbose_name="Action Time")
    Action = models.TextField(verbose_name="Action")

    def __str__(self):
        return str(self.TAHID)

class Expense(models.Model):
    ExpenseID = models.AutoField(primary_key=True)
    Expense = models.CharField(max_length=255, verbose_name='Expense', null=True, blank=True)

    def __str__(self):
        return self.Expense













