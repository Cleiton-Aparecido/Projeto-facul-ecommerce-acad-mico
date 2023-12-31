"""appYoutube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth import views
from django.urls import path
from task import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tasks, name='task'),
    # path('', views.sigin, name='sigin'),
    path('admin/', admin.site.urls),
    path('sigin/', views.sigin, name='sigin'),
    path('task/', views.tasks, name='task'), 
    path('home/', views.tasks, name='home'),
    path('sigup/', views.sigup, name='sigup'),
    path('sair/', views.sair, name='sair'),
    path('tasks/', views.tasks, name='tasks'),
    path('vender/', views.venda, name='venda'),
    path('publicar-item/', views.publicar_item_venda, name='publicar-item'),
    path('consulta-itens-vendas/', views.tasks, name='consulta_itensVendas'),

]

