from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("kvak/", include("kvak.urls")),
    path("admin/", admin.site.urls),
]