# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from finger_db.models import Request
from django.http import HttpRequest
from django.http import HttpResponse
from UserData.models import User
from datetime import datetime
import re
from django.http import JsonResponse
import json
from django.core import serializers
from django.utils.safestring import mark_for_escaping
from django.forms.models import model_to_dict
from django.contrib.gis.geoip2 import GeoIP2
from ipware.ip import get_real_ip


def index(request):
    context = {}
    return render(request, 'index copy.html', context)


def fingerprint(request):
    isLogin = request.session.get('isLogin', False)
    if isLogin:

        context = {}
    # regex_http_ = re.compile(r'^HTTP_.+$')
    # request_headers = {}
    # for header in request.META:
    #     if regex_http_.match(header) :
    #         request_headers[header] = request.META[header]
    #
    # key_list = request_headers.keys()
    # get the whole log content from log file
        filename = '/var/log/apache2/forensic_log1'
        with open(filename) as f:
            log = f.read()
        # save the latest GET
        get_regex = re.compile(r'\|GET /fingerprint HTTP/1.*\n')
        get_list = get_regex.findall(log)
        get_latest = get_list[-1]
    # save all the key-values in the latest GET
        regex = re.compile(r'.*(?=:)')
        elements = get_latest.split('|')[2:]
        headerList = []
        for e in elements:
            key = regex.findall(e)[0]
            headerList.append(key)
            # list = regex.findall(get_latest)
        context['HeaderList'] = ' || '.join(headerList)

        request.session['headerList'] = headerList

        user_agent = request.META.get('HTTP_USER_AGENT')
        acceptType = request.META.get('HTTP_ACCEPT')
        acceptEncoding = request.META.get('HTTP_ACCEPT_ENCODING')
        acceptLanguage = request.META.get('HTTP_ACCEPT_LANGUAGE')
        dnt =request.META.get('HTTP_DNT', 0)
        IP = request.META.get('REMOTE_ADDR')
        context['a'] =request.META
        context['UserAgent'] = user_agent
        context['AcceptType'] = acceptType
        context['AcceptEncoding'] = acceptEncoding
        context['AcceptLanguage'] = acceptLanguage
        context['dnt'] = dnt
        context['IP'] = IP


        g = GeoIP2('GeoLite2-City_20170801')
        context['country'] = g.city(IP)['country']


        email = request.session.get('email', '')
        ID = request.session.get('id','')
        context['id'] = ID
        context['email'] = email
        request.session['UserAgent'] = request.META.get('HTTP_USER_AGENT')
        request.session['AcceptType'] = request.META.get('HTTP_ACCEPT')
        request.session['AcceptEncoding'] = request.META.get('HTTP_ACCEPT_ENCODING')
        request.session['AcceptLanguage'] = request.META.get('HTTP_ACCEPT_LANGUAGE')
        return render(request, 'pages/blank.html', context)

    else:
         return HttpResponse('Sorry，you need to login')


def table(request):
    context = {}
    email = request.session.get('email')
    ID = request.session.get('id')
    context['email'] = email
    context['id'] = ID
    context['isLogin'] = request.session.get('isLogin',False)
    return render(request, 'pages/tables.html', context)


def ajax_list(request):
    a = list(range(100))
    return HttpResponse(json.dumps(a), content_type='application/json')


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')


def table_update(request):
    if request.method == "POST":
        context = {}

        email = request.session.get('email')
        id = request.session.get('id')

        u = User.objects.get(email=email, UID=id)
        context['email'] = email
        context['id'] = id
        records = Request.objects.filter(browserID=u).values('id', 'AcceptLanguage')
        records_dict = list(records)
        return JsonResponse(records_dict, safe=False)


def scene_update_view(request):
    if request.method == "POST":
        fp = request.POST.get('FingerPrint')
        u = User.objects.get(email=request.session.get('email',''), UID=request.session.get('id',''))
        exist = Request.objects.filter(browserID=u, FingerPrint=fp).exists()
        if exist:
            record =  Request.objects.filter(browserID=u, FingerPrint=fp)[0]
            record.count+=1
            record.save()
        else:
            record = Request()
            record.UserAgent_in_the_request = request.session.get('UserAgent')
            record.AcceptType = request.session.get('AcceptType')
            record.AcceptEncoding = request.session.get('AcceptEncoding')
            record.AcceptLanguage = request.session.get('AcceptLanguage')
            record.DNT = request.META.get('HTTP_DNT', 0)
            headerList = request.session.get('headerList')
            record.HeaderOrder = ' || '.join(headerList)
            record.time = str(datetime.now())
            record.IPAddress = request.META.get('REMOTE_ADDR')
            record.User_Agent_obtained_by_JS = request.POST.get('UserAgent')
            record.OS = request.POST.get('OS')
            record.OS_Version = request.POST.get('OS_Version')
            record.Browser = request.POST.get('Browser')
            record.BrowserVersion = request.POST.get('Browser_Version')
            record.TimeZone = request.POST.get('TimeZone')
            record.Font = request.POST.get('Font')
            record.Plugins = request.POST.get('Plugins')
            record.ScreenResolution = request.POST.get('Screen_Resolution')
            record.FlashEnabled = request.POST.get('Flash')
            record.Flash_Version = request.POST.get('Flash_Version')
            record.Color_Depth = request.POST.get('Color_Depth')
            record.CookiesEnabled = request.POST.get('CookiesEnabled')
            record.Language = request.POST.get('language')
            record.Canvas = request.POST.get('Canvas')
            record.AspectRation = request.POST.get('AspectRatio')
            record.ZoomRatio = request.POST.get('ZoomRatio')
            record.AvailableViewArea = request.POST.get('AvailableViewArea')
            record.FingerPrint = request.POST.get('FingerPrint')
            record.AdBlock = request.POST.get('AdBlock')
            record.isJava = request.POST.get('isJava')
            record.isLocalStorage = request.POST.get('isLocalStorage')
            record.isSessionStorage = request.POST.get('isSessionStorage')
            record.browserID = u
            u.FPList += ',' + str(record.FingerPrint)
            u.Browser = record.Browser
            u.OS = record.OS
            u.save()
            # times = Request.objects.filter(browserID=u).count()+1
            #     j = {'status': 'new', 'browserID': u.id, 'sessionID': times,'isLogin':1}
            # else :
            #     j={'status':'anonymous','isLogin':0}
            record.save()

        j={'status':'anonymous','isLogin':0}

        return HttpResponse(json.dumps(j), content_type='application/json')


def test(request):
    context = {}
    u = User.objects.filter(email='495130811@qq.com').values('email')
    print u
    return render(request, 'pages/buttons.html', context)


def statistics(request):
    context = {}
    email = request.session.get('email')
    ID = request.session.get('id')
    context['email'] = email
    context['ID'] = ID

    # OS names list in the data set
    OS = Request.objects.values('OS').distinct()
    print OS
    OSlist = []
    OSnumber = []
    for e in list(OS):
        OSname = e.get('OS').encode('ASCII', 'ignore')
        OSlist.append(OSname)
        OSlength = len(list(Request.objects.values('OS')))
        number = float(Request.objects.filter(OS=OSname).count())/OSlength
        OSnumber.append(number)

    # Browser name
    Browser = Request.objects.values('Browser').distinct()
    Blist = []
    Bnumber = []
    for e in list(Browser):
        tmp = e.get('Browser').encode('ASCII', 'ignore')
        Blist.append(tmp)
        number = Request.objects.filter(Browser=tmp).count()
        Bnumber.append(number)
    context['OSlist'] = OSlist
    context['OSnumber'] = OSnumber
    context['Blist'] = Blist
    context['Bnumber'] = Bnumber

    # return render_to_response('pages/Statistics.html',context,context_instance=RequestContext(request))
    return render(request, 'pages/Statistics.html', context)

def home(request):
    context = {}
    email = request.session.get('email')
    ID = request.session.get('id')
    context['email'] = email
    context['ID'] = ID
    return render(request, 'pages/index.html', context)


