# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import SettingWeb
from .serializers import SettingWebSerializer

# Create your views here.
def testing_api(request):
	return JsonResponse({'prop1': 'halo'})

def setting_web(request):
	setting_web_queryset = SettingWeb.objects.all()
	setting_web_serializer = SettingWebSerializer(setting_web_queryset, many=True)
	return JsonResponse(setting_web_serializer.data, safe=False)