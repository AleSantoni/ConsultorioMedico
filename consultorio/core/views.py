from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect




class HomePageView(TemplateView):
    template_name= 'core/index.html'
class AdminPageView(TemplateView):
    template_name= 'core/IndexAdmin.html'
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.request.user
        if user.is_superuser or user.is_staff:
            return redirect('IndexAdmin')  # Cambia 'admin_home' según tus necesidades
        else:
            return redirect('index')  # Cambia 'user_home' según tus necesidades