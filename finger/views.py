from finger_db.models import Request,User
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

class table(TemplateView):
    template_name = 'pages/tables.html'

class UsersListJson(BaseDatatableView):
    model = Request
    columns = ['time','HeaderOrder','UserAgent_in_the_request','AcceptType','AcceptEncoding','AcceptLanguage','IPAddress','DNT']
    order_columns = ['time','HeaderOrder','UserAgent_in_the_request','AcceptType','AcceptEncoding','AcceptLanguage','IPAddress','DNT']

    def filter_queryset(self, qs):
        email = self.request.session.get('email', None)
        id = self.request.session.get('id',None)
        u =  User.objects.get(email=email,UID=id)
        qs = qs.filter(browserID = u)
        return qs

class TableJson(BaseDatatableView):
    model = Request
    columns = ['time','User_Agent_obtained_by_JS','OS','OS_Version','Browser','BrowserVersion','ScreenResolution','Plugins','Font','TimeZone','CookiesEnabled','Color_Depth','Language','Canvas','AdBlock','isJava','isLocalStorage','isSessionSorage']
    # order_columns = ['time','User_Agent_obtained_by_JS','OS','OS_Version','Browser','BrowserVersion']

    def filter_queryset(self, qs):
        email = self.request.session.get('email', None)
        id = self.reque#!/usr/bin/python



st.session.get('id',None)
        u =  User.objects.get(email=email,UID=id)
        qs = qs.filter(browserID = u)
        return qs