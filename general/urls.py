from django.urls import path
from.views import *

urlpatterns = [
    path('',homepage,name='index'),
    path('about',about,name='about'),
    path('service',service,name='service'),
    path('project',project,name='project'),
    path('blog',blog,name='blog'),
    path('contact',contact,name='contact')
]
