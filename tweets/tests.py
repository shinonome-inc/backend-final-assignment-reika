from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

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
    url_name = "tweets:create"

    def test_success_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_success_post(self):
        valid_data = {"content": "test tweet"}
        response = self.client.post(self.url, valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "tweets/home/")


#    def test_failure_post_with_empty_content(self):

#    def test_failure_post_with_too_long_content(self):


# class TestTweetDetailView(TestCase):
#    def test_success_get(self):


# class TestTweetDeleteView(TestCase):
#    def test_success_post(self):

#    def test_failure_post_with_not_exist_tweet(self):

#    def test_failure_post_with_incorrect_user(self):


# class TestLikeView(TestCase):
#    def test_success_post(self):

#    def test_failure_post_with_not_exist_tweet(self):

#    def test_failure_post_with_liked_tweet(self):


# class TestUnLikeView(TestCase):

#    def test_success_post(self):

#    def test_failure_post_with_not_exist_tweet(self):

#    def test_failure_post_with_unliked_tweet(self):
