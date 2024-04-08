from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from vegastroy.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from vegastroy.accounts.models import Profile


UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register_page.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login_page.html'

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class UserLogoutView(LogoutView):
    pass


class UserDetailView(views.DetailView):
    model = UserModel
    template_name = 'accounts/details_page.html'


class UserEditView(views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'accounts/edit_page.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy(
            'profile_details',
            kwargs={
                'pk': self.object.pk
            }
        )


class UserDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/delete_page.html'
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())
