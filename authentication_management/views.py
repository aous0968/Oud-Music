import json

from django.db import IntegrityError
from .forms import RegisterForm, CustomAuthenticationForm

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class MyLoginView(LoginView):
    
    redirect_authenticated_user = True
    authentication_form = CustomAuthenticationForm

    def get_success_url(self) -> str:
        return reverse_lazy('home')


@csrf_exempt
def username_validation(request):
    if request.method == "POST":
        user_name = request.POST.get('req_data')
        data = {
            "massage": "The user name is valid.",
            "good": True
        }
        try:
            User.objects.get(username=user_name)
        except User.DoesNotExist:
            data["massage"] = "the user name does not exist."
            data["good"] = False
            return HttpResponse(json.dumps(data))

        return HttpResponse(json.dumps(data))

    return HttpResponse("the method is not post.")


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/reset/password_reset.html'
    email_template_name = 'registration/reset/password_reset_email.html'
    subject_template_name = 'registration/reset/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('password_reset')


def register(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm(request.POST or None)

    context = {'form': form}

    if request.POST:
        if form.is_valid():
            user_name = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                get_user_model().objects.create_user(username=user_name, email=email,
                                                    password=password, first_name=first_name, last_name=last_name)
            except IntegrityError:
                form.add_error(None , "user name must be unipue")
                return render(request, "registration/register.html", context)
                
            user = authenticate(username=user_name, password=password)
            login(request, user)
            return redirect("My_login")

    return render(request, "registration/register.html", context)

@csrf_exempt
def username_unique(request):
    if request.method == "POST":
        user_name = request.POST.get('req_data')
        data = {
            "massage": "user name must be unique",
            "good": False
        }
        try:
            user_name = user_name.strip()
            if user_name.isspace() or not user_name:
                raise Exception("empty string")
            User.objects.get(username=user_name)
        except User.DoesNotExist:
            data["massage"] = "the user name is valid."
            data["good"] = True
            return HttpResponse(json.dumps(data))
        except : 
            return HttpResponse(json.dumps(data))


        return HttpResponse(json.dumps(data))

    return HttpResponse("the method is not post.")