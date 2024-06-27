from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tweet

User = get_user_model()


class TestHomeView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.url = reverse("tweets:home")

    def test_success_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class TestTweetCreateView(TestCase):
    url_name = reverse("tweets:create")

    def test_success_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_success_post(self):
        valid_data = {"content": "test tweet"}
        response = self.client.post(self.url, valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/tweets/home/")

    def test_failure_post_with_empty_content(self):
        invalid_data = {"content": ""}
        response = self.client.post(self.url, invalid_data)

        form = response.context{"form"}

        self.assertEqual(response.status_code, 200)
        self.assertFalse(form.is_valid())

        self.assertIn("このフィールドは必須です。", form.errors["content"])


    def test_failure_post_with_too_long_content(self):
        invalid_data = {"context" : "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
        response = self.client.post(self.url, invalid_data)
        form = response.context{"form"}

        self.assertEqual(response.status_code, 200)
        self.assertFalse(form.is_valid())

        self.assertIn("長すぎます。", form.errors["content"])


class TestTweetDetailView(TestCase):
    is_need_kwargs = True
    url_name = reverse("tweets:detail")
    
    def test_success_get(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Tweet.objects.filter(content=self.tweet1.content).exists())


class TestTweetDeleteView(TestCase):
    is_need_kwargs = True
    url_name = reverse("tweets:delete")

    def test_success_post(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("tweets:home"))
        self.assertFalse(Tweet.objects.filter(pk=self.tweet1.pk).exists())

    def test_failure_post_with_not_exist_tweet(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 404)

#    def test_failure_post_with_incorrect_user(self):


# class TestLikeView(TestCase):
#    def test_success_post(self):

#    def test_failure_post_with_not_exist_tweet(self):

#    def test_failure_post_with_liked_tweet(self):


# class TestUnLikeView(TestCase):

#    def test_success_post(self):

#    def test_failure_post_with_not_exist_tweet(self):

#    def test_failure_post_with_unliked_tweet(self):
