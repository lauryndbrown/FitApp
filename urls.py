from django.conf.urls import include url
from django.contrib import admin

urlpatterns = [
		url(r'^fit/', include('fit.urls')),
		url(r'^admin/', admin.site.urls),
]
