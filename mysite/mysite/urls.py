
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^rex/', include('rex.urls')),
    url(r'^admin/', admin.site.urls),
]
