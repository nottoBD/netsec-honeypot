from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/', permanent=False)),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    ]

