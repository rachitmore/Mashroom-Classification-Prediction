from django.urls import path
from . import views

app_name = 'mashroom_classify'

urlpatterns = [
    path('', views.home, name='home'),

]
