from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("mail/", include(("mail.urls", "mail"), namespace="mail")),
    path("network/", include(("network.urls", "network"), namespace="network")),
]
