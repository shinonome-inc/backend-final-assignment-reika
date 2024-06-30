from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, TemplateView

from tweets.forms import CreateTweetForm

from .models import Tweet


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "tweets/home.html"


class TweetCreateView(CreateView):
    model = Tweet
    form_class = CreateTweetForm
    template_name = "tweets/create.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TweetDetailView(DetailView):
    model = Tweet
    template_name = "tweets/detail.html"
    context_object_name = "tweet"

    def get_queryset(self):
        return Tweet.objects.filter(author=self.request.user)


class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = "tweets/delete.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user
