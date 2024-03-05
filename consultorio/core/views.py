
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from servicios.models import Servicios
from medicos.models import Medico




from especialidades.views import *
from django.contrib.auth.views import LoginView




    
class CustomLoginView(LoginView):
    def get_success_url(self):
        # Personaliza la URL de redirección después del inicio de sesión según el tipo de usuario
        if self.request.user.is_superuser or self.request.user.is_staff:
            return '/IndexAdmin/'
        else:
            return '/'


class HomePageView(TemplateView):
    template_name = 'core/index.html'
   
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = Especialidades.objects.all()  # Obtén todas las especialidades
        context['medicos'] = Medico.objects.all()  # Obtén todos los médicos
        context['especialidades_count'] = Especialidades.objects.count()
        context['medicos_count'] = Medico.objects.count()
    
        context['Servicios'] = Servicios.objects.all()
        return context

class AdminPageView(TemplateView):
    template_name = 'core/indexAdmin.html'


def ValidarUsuario(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            return redirect('/IndexAdmin/')
        else:
            return redirect('/')  # Reemplaza '/otra-pagina/' con la URL que desees para usuarios no staff ni superuser
    return redirect('login')

