from django.urls import path
from .views import *

app_name = 'notepad'

urlpatterns = [
    path('',index_view,name='home'),
    path('save/',form_view,name='forms')
]
