
from django.urls import path
from .views import CustomLoginView, HomePageView,AdminPageView

urlpatterns = [
   path('', HomePageView.as_view(), name='index'),
     path('IndexAdmin/', AdminPageView.as_view(), name='IndexAdmin'),
   path('login/', CustomLoginView.as_view(), name='login'),
 
   
   
   
   
]