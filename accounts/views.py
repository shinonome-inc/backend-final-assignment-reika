from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("tweets:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

    def signup(request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tweets:home')
        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})
