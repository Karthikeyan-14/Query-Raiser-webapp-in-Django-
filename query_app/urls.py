"""
URL configuration for query_raiser_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import views

urlpatterns = [
    path('', views.start),

    path('start',views.start,name='go-start'),

    path('login',views.login,name='login'),
    path('regs',views.reg,name='register'),

    path('log',views.log,name='go-log'),
    path('dash',views.go_dash,name='go-dash'),

  

    path('modal',views.modal,name='modal_view'),

    path('response',views.responses,name='response_data'),

    path('responded',views.fetch_res,name='respond_to'),

    path('status',views.update,name='update_status'),

    path('modall',views.modal2,name='modal2_view'),

    path('admin_res',views.adm_res,name='admin_response_data'),


    path('save',views.save_res,name='save_response'),

    path('saved',views.save_data,name='save_query'),

    path('getque',views.get_question,name='get_ques'),

    path('reports',views.report_data,name='report')

]
