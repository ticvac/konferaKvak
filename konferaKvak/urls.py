from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("kvak/", include("kvak.urls")),
    path("admin/", admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()