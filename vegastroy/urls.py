from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vegastroy.web.urls')),
    path('accounts/', include('vegastroy.accounts.urls')),
    path('ask_for_offer/', include('vegastroy.ask_for_offer.urls')),
    path('contacts/', include('vegastroy.contacts.urls')),
    path('our_projects/', include('vegastroy.projects.urls')),
    path('blog/', include('vegastroy.blog.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'vegastroy.web.views.custom_404'
