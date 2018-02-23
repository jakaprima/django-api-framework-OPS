from django.conf.urls import url, include

from .views import testing_api, setting_web

urlpatterns = [
	url(r'^$', testing_api),
	url(r'^settingweb/', setting_web),
]