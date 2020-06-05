from django.shortcuts import render
from django.views.generic import CreateView
from user.forms import SignUpForm, AdminSignUpForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views.generic import FormView, View
from django.contrib.auth.forms import AuthenticationForm

# login to admin or GraduateAccount
class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'account/login.html'
	success_url = reverse_lazy('graduateHome')
	def form_valid(self, form):
		# login user
		email, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
		user = authenticate(email=email, password=password)
		if user is not None:
			if user.is_staff:
				success = reverse_lazy('adminHome')
			else:
				success = reverse_lazy('graduateHome')
			login(self.request, user)
			return redirect(success)

# logout and redirect to login or home
class LogoutView(View):
	success_url = reverse_lazy('logout')
	def get(self, request):
		logout(request)
		return redirect('/login')

# register an GraduateAccount
class SignupView(CreateView):
	form_class = SignUpForm
	template_name = 'account/signup.html'
	success_url = reverse_lazy('graduateHome')

	def form_valid(self, form):
		# save account first
		account = form['account'].save()
		profile = form['graduateProfile'].save(commit=False)
		profile.account = account
		folder = form['graduateFolder'].save()
		profile.folder = folder
		profile.save()
		# login user
		login(self.request, account)
		return redirect(reverse_lazy('graduateHome'))

# register an adminUser
class AdminSignupView(CreateView):
	form_class = AdminSignUpForm
	template_name = 'account/signup-admin.html'

	def form_valid(self, form):
		# save account
		account = form['account'].save(commit=False)
		account.is_staff=1
		account.save()
		profile = form['adminProfile'].save(commit=False)
		profile.account = account
		profile.save()
		# login user
		login(self.request, account)
		return redirect(reverse_lazy('adminHome'))

