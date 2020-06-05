from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm, AdminSignUpForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views.generic import FormView, View, ListView
from django.contrib.auth.forms import AuthenticationForm

# render homepage school-service
class AdminHomeView(View):
	def get(self, request):
		if request.user.is_authenticated:
			if request.user.user_type == 'adm-serv':
				return render(request, 'home/service/inicio.html')
			elif request.user.user_type == 'adm-coord':
				return render(request, 'home/coordinate/inicio.html')
		else:
			return redirect(reverse_lazy('login'))

