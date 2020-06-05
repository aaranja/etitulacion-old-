from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin, UserPassesTestMixin
from django.contrib.auth import logout
from django.shortcuts import render
from django.views.generic import FormView, View, TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import UploadDocs
import os
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class RedirectIfIsStaffMixin(AccessMixin):
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_staff==1:
			logout(request)
			return self.handle_no_permission()
		return super(LogoutIfNotStaffMixin, self).dispatch(request, *args, **kwargs)

class TestAccessUser(UserPassesTestMixin):                         
    def test_func(self):
    	self.object = self.get_object()
    	print("aloooooooooooooooooooooo")
    	return self.request.user.is_staff == 0

# render home page graduate
class HomeView(View):
	def get(self, request):
		print(request.user.is_staff)
		if request.user.is_staff:
			return redirect(reverse_lazy('adminHome'))
		else:
			return render(request, 'graduate/home.html')

class UploadFiles(FormView):
	form_class = UploadDocs
	template_name = 'graduate/upload-documents.html'

	# set initial to delete document upload 
	def get_initial(self):
		# default path
		folder='documents/'
		initial = super(FormView, self).get_initial()

		try:
			current_user = self.request.user
			folder = folder+str(current_user.graduate_profile.enrollment)+'/'
			if os.path.exists(folder) is False:
				os.mkdir(folder)
			else:
				# set default true or false if document is upload
				initial['borrar_acta'] = self.find_document('acta_de_nacimiento', folder)
				initial['borrar_curp'] = self.find_document('cURP', folder)
				initial['borrar_cdi'] = self.find_document('certificado_de_ingles', folder)
				initial['borrar_cdb'] = self.find_document('certitificado_de_bachiller', folder)
		except:
			print('La carpeta ya existe')
		print(initial)
		return initial

	# save or delete documents uploads
	def form_valid(self, form):
		# default path
		folder='documents/'
		try:
			current_user = self.request.user
			folder = folder+str(current_user.graduate_profile.enrollment)+'/'
			if os.path.exists(folder) is False:
				os.mkdir(folder)
		except:
			print('La carpeta ya existe')

		# print(form.cleaned_data['borrar_acta'])
		# delete document if checkbox is true
		if(form.cleaned_data['borrar_acta']):
			self.delete_document('acta_de_nacimiento', folder)
		if(form.cleaned_data['borrar_curp']):
			self.delete_document('cURP', folder)
		if(form.cleaned_data['borrar_cdi']):
			self.delete_document('certificado_de_ingles', folder)
		if(form.cleaned_data['borrar_cdb']):
			self.delete_document('certitificado_de_bachiller', folder)

		# save files in egresado id folder
		for name_doc in self.request.FILES:
			doc = self.request.FILES[name_doc]
			fs = FileSystemStorage(location=folder)

			# check if document exist in folder and delete to override 
			self.delete_document(name_doc, folder)

			filename = fs.save(name_doc+'.pdf', doc)
			file_url = fs.url(filename)
		return redirect(reverse_lazy('graduateHome'))

	# delete document if exist
	def delete_document(self, name_doc, folder):
		for file in os.listdir(folder):
			if file.startswith(name_doc):
				os.remove(folder+file)

	# return false if file don't exist
	def find_document(self, name_doc, folder):
		for file in os.listdir(folder):
			if file.startswith(name_doc):
				return False
		return True