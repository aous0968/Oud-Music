from django.urls import path
from OudMusic import settings
# from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from authentication_management.views import (
    register,
    username_validation,
    username_unique,
    MyLoginView,
    ResetPasswordView,
)


urlpatterns = [
    path("register/", register, name="register"),
    path("register/username-unique/", username_unique , name="username_unique"),
    path("login/", MyLoginView.as_view(), name="My_login"),
    path("login/username-validation/", username_validation , name="username_validation"),
    path("logout/", auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    path("password-reset/", ResetPasswordView.as_view(), name="password_reset"),
    path("password-reset-confirm/<uidb64>/<token>/",  auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
