from django.urls import path, include, url
from . import views

from apps.usuario.views import index ,usuario_view

"""
urlpatterns = [   
    path('', views.post_list),
"""

urlpatterns = [
    url(r'^nuevo$',usuario_view,name='usuario_crear')
]