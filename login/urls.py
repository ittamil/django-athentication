from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('dontlookback/', admin.site.urls),
    path('',include('accounts.urls'))
]
handler404 = 'accounts.views.error404'

