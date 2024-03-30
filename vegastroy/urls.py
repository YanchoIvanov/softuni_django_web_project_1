from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vegastroy.web.urls')),
    path('accounts/', include('vegastroy.accounts.urls')),
    path('ask_for_offer/', include('vegastroy.ask_for_offer.urls')),
    path('contacs/', include('vegastroy.contacts.urls')),

]

handler404 = 'vegastroy.web.views.custom_404'
