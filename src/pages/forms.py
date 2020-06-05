from django import forms
from django.forms import ModelForm

class UploadDocs(forms.Form):
	acta_de_nacimiento = forms.FileField(widget=forms.ClearableFileInput(attrs={'value': 'acta', 'accept':'image/png,image/gif,image/jpeg, application/pdf'}), required=False)
	cURP = forms.FileField(widget=forms.ClearableFileInput(attrs={'value': 'curp','accept':'image/png,image/gif,image/jpeg, application/pdf'}), required=False)
	certificado_de_ingles = forms.FileField(widget=forms.ClearableFileInput(attrs={'value': 'cdi','accept':'image/png,image/gif,image/jpeg, application/pdf'}), required=False)
	certitificado_de_bachiller = forms.FileField(widget=forms.ClearableFileInput(attrs={'value': 'cdb','accept':'image/png,image/gif,image/jpeg, application/pdf'}), required=False)

	borrar_acta = forms.BooleanField(label="Borrar",initial=False, required=False, widget=forms.CheckboxInput(attrs={'class':'delet-box', 'id':'actaD'}))
	borrar_curp = forms.BooleanField(label="Borrar",initial=True, required=False, widget=forms.CheckboxInput(attrs={'class':'delet-box', 'id':'curpD'}))
	borrar_cdi = forms.BooleanField(label="Borrar",initial=True, required=False, widget=forms.CheckboxInput(attrs={'class':'delet-box','id':'cdiD'}))
	borrar_cdb = forms.BooleanField(label="Borrar",initial=True, required=False, widget=forms.CheckboxInput(attrs={'class':'delet-box','id':'cdbD'}))

class AccurateDocs(forms.Form):
	birth_certificate = forms.BooleanField(label="Acta de nacimiento",initial=False, required=False, widget=forms.CheckboxInput())
	curp = forms.BooleanField(label="C.U.R.P",initial=False, required=False, widget=forms.CheckboxInput())
	degree_certificate = forms.BooleanField(label="Certificado de licenciatura",initial=False, required=False, widget=forms.CheckboxInput())
	hschool_certificate = forms.BooleanField(label="Certificado de bachillerato",initial=False, required=False, widget=forms.CheckboxInput())