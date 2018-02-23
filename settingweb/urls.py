from django.conf.urls import url, include

from .views import setting_web
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', setting_web),
]
