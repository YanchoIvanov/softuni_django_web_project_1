from django.urls import path, include

from vegastroy.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, UserDetailView, UserEditView, \
    UserDeleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailView.as_view(), name='profile_details'),
        path('edit/', UserEditView.as_view(), name='profile_edit'),
        path('delete/', UserDeleteView.as_view(), name='profile_delete'),
    ])),
]
