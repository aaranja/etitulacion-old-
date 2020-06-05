from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Account, GraduateProfile, AdminProfile, GraduateFolder
from betterforms.multiform import MultiModelForm
from django.utils.translation import ugettext_lazy as _

# graduate register
class AccountForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = Account
		fields = ('email', 'password1', 'password2')
		widgets = {
		'email'			:	forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Correo electrónico'}),
		'password1'		:	forms.PasswordInput(attrs={'class': 'form-control','type':'password'}),
		'password2'     :	forms.PasswordInput(attrs={'class': 'form-control','aria-describedby':'passwordHelpInline'}),
		}

class AdminProfileForm(ModelForm):
	class Meta:
		model = AdminProfile
		fields = ('enrollment', 'first_name', 'last_name','admin_type')
		labels = {
		'enrollment': _('No. de empleado'),
		'admin_type': _('Tipo de usuario'),
		}
		ADMIN_TYPE_CHOICE = [
		('nochoose',   'Elegir...'),
		('adm-serv',   'Servicios Escolares'),
		('adm-coord',   'Coordinación de titulación'),
		]
		widgets = {
		'first_name'	:	forms.TextInput( attrs={'class': 'form-control', 'placeholder':'Nombre(s)'}),
		'last_name'		:	forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Apellido(s)'}),
		'enrollment'	:	forms.NumberInput(attrs={'class': 'form-control'}),
		'admin_type'	:	forms.Select(choices=ADMIN_TYPE_CHOICE, attrs={'class':'custom-select'}),
		}

class GraduateProfileForm(ModelForm):
	class Meta:
		model = GraduateProfile
		fields = ('enrollment', 'first_name', 'last_name', 'career', 'gender')
		labels = {
			'enrollment'	:	_('Matrícula'),
			'first_name'	:	_('Nombre(s)'),
			'last_name'		:	_('Apellido(s)'),
            'career'		:	_('Carrera'),
            'gender'		:	_('Género'),
        }
		CAREER_CHOICE = [
			('0',   'Elegir...'),
			('Ing. Electromecánica',			'Ing. Electromecánica'),
			('Ing. Electrónica',   				'Ing. Electrónica'),
			('Ing. Gestión Empresarial',		'Ing. Gestión Empresarial'),
			('Ing. Industrial',					'Ing. Industrial'),
			('Ing. Mecatrónica',				'Ing. Mecatrónica'),
			('Ing. Sistemas Computacionales',	'Ing. Sistemas Computacionales'),
			('Lic. Administración',				'Lic. Administración'),
		]
		GENDER_CHOICE = [
			('0', 'Elegir...'),
			('Femenino', 'Femenino'),
			('Masculino', 'Masculino'),
			('Otro', 'Otro'),
		]
		widgets = {
		'first_name'	:	forms.TextInput( attrs={'class': 'form-control', 'placeholder':'Nombre(s)'}),
		'last_name'		:	forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Apellido(s)'}),
		'enrollment'	:	forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'12345678'}),
		'career'		:	forms.Select(choices=CAREER_CHOICE, attrs={'class':'custom-select'}),
		'gender'		:	forms.Select(choices=GENDER_CHOICE, attrs={'class': 'custom-select'})
		}
# accurate form for services
class AccurateFolderForm(ModelForm):
	class Meta(object):
		model = GraduateFolder

		fields = ('birth_certificate','curp','degree_certificate','hschool_certificate')
		labels = {
			'birth_certificate'		:	_('Acta de nacimiento'),
			'curp'					:	_('C.U.R.P'),
			'degree_certificate'	:	_('Certificado de licenciatura'),
			'hschool_certificate'	:	_('Certificado de bachillerato'),
			}
		widgets = {
			'birth_certificate'		:	forms.CheckboxInput(attrs={'class':'delet-box',  'checked' : ''}),
			'curp'		:	forms.CheckboxInput(attrs={'class':'delet-box',  'checked' : 'False'})
		}

# form for register
class GraduateFolderForm(ModelForm):
	class Meta:
		model = GraduateFolder
		fields = ()

class SignUpForm(MultiModelForm):
	form_classes = {
		'graduateProfile': GraduateProfileForm,
		'account': AccountForm,
		'graduateFolder' : GraduateFolderForm
	}

class AdminSignUpForm(MultiModelForm):
	form_classes = {
		'account': AccountForm,
		'adminProfile': AdminProfileForm,
	}
