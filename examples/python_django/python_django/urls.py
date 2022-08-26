from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/didkit')),
    path('didkit/', include('didkit_django.urls')),
    path('admin/', admin.site.urls),
]
