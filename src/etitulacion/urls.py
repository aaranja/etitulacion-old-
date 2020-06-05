"""etitulacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import LoginView, LogoutView, SignupView, AdminSignupView
import pages.graduate_views as Graduate
import pages.services_views as Services
from django.conf.urls import url, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('registro/', SignupView.as_view(), name = 'signup'),
    path('registro-admin/', AdminSignupView.as_view(), name = 'signupAdmin'),
    path('logout/',LogoutView.as_view(), name='logout' ),
    path('inicio/egresado', Graduate.HomeView.as_view(), name = 'graduateHome'),
    path('inicio/egresado/subir-documentacion', Graduate.UploadFiles.as_view(), name = 'uploadGraduateDocs'),
    path('inicio/servicios-escolares/', Services.TableView.as_view(), name='adminHome' ),
    path('inicio/servicios-escolares/validar-documentos/<int:id>/', Services.ApproveView.as_view(), name='servApprove' ),
    path('inicio/servicios-escolares/<int:id>/carta-no-inconveniencia/', Services.some_view, name='downloadLetter'),
]
