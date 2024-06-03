from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tweets:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response

    def form_invalid(self, form):
        return super().form_invalid(form)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profiles/profile.html"
    login_url = "registration/login.html"

    def get(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context
