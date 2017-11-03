"""finger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from . import view
from django.contrib import admin
from UserData import views
from .views import  TableJson, UsersListJson
urlpatterns = [
    url(r'^$', view.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^table$', view.table, name='table'),
    url(r'^fingerprint$', view.fingerprint, name='fp'),
    #url(r'^add/$',view.deal,name='add'),
    url(r'^scene_update_view/', view.scene_update_view, name='scene_update_view'),
    url(r'^register$', views.register, name='register'),
    url(r'^register_update_view/',views.register_update,name='register_update_view'),
    url(r'^login$', views.login, name='login'),
    url(r'^test$', view.test, name='test'),
    url(r'^get_info/', view.table_update, name='get_info'),
    url(r'^users_data/$', UsersListJson.as_view(), name="table_data_1"),
    url(r'^table_data_2/$', TableJson.as_view(), name="table_data_2"),
    url(r'^statistics$', view.statistics, name="statistics"),
    url(r'^home', view.home, name="home"),

    #url(r'^accounts/', include('users.urls')),
]
