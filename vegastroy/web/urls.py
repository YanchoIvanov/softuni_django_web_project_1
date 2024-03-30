from django.urls import path

from vegastroy.web.views import home

urlpatterns = [
    path('', home, name='home_page')

]