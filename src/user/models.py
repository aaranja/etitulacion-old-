from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class Account(AbstractUser):
	# pk
	account_id = models.AutoField(primary_key=True)
	# unnecessary data
	first_name = None
	last_name = None
	username = None
	# set email as username
	email = models.EmailField(_('email address'), unique=True)	# set email=unique and blank=false
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

class GraduateFolder(models.Model):
	folder_id = models.AutoField(primary_key=True)
	birth_certificate = models.BooleanField(default=False)
	english_certificate = models.BooleanField(default=False)
	hschool_certificate = models.BooleanField(default=False)
	degree_certificate = models.BooleanField(default=False)
	curp = models.BooleanField(default=False)
	constancy_ni = models.BooleanField(default=False)
	titulate_document = models.BooleanField(null=True)

class GraduateProfile(models.Model):
	# pk
	enrollment = models.IntegerField(primary_key=True, unique=True, blank=False)
	# graduate data
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=150)
	career = models.CharField(max_length=30, blank=True)
	gender = models.CharField(max_length=10, blank=True)
	type_degree = models.CharField(max_length=30, blank=True, null=True)
	status = models.CharField(max_length=30, blank=True, null=True)
	accurate_docs = models.BooleanField(default=False)
	# fk
	folder = models.OneToOneField(GraduateFolder,on_delete=models.CASCADE, related_name="graduate_folder") # relational with Perfil model
	account = models.OneToOneField(Account,on_delete=models.CASCADE, related_name="graduate_profile") # relational with Perfil model


class AdminProfile(models.Model):
	# pk
	enrollment = models.IntegerField(primary_key=True, unique=True, blank=False)
	# graduate data
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=150)
	# user type : 'graduate', 'adm-coord', 'adm-serv'
	admin_type = models.CharField(max_length=10)
	# fk
	account = models.OneToOneField(Account,on_delete=models.CASCADE, related_name="admin_profile") # relational with Perfil model

	