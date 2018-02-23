from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def setting_web(request):
	return JsonResponse({'halo':'halo'})