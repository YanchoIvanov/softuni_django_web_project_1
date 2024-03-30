from django.urls import path

from vegastroy.contacts.views import contacts_page

urlpatterns = [
    path('', contacts_page, name='contacts_page'),

]
