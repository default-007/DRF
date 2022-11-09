from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class PostTests(APITestCase):
    def test_view_post(self):
        """
        Ensure we can view all objects
        """
        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        """
        Ensure we can create a new post object and view object
        """
        self.test_category = Category.objects.create(name="django")
        self.testuser = User.objects.create_user(
            username="testuser", password="1234567"
        )
        self.client.login(username=self.testuser1.username, password="1234567")
        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse("blog_api:listcreate")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        root = reverse(("blog_api:detailcreate"), kwargs={"pk": 1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        client = APIClient()

        self.test_category = Category.objects.create(name="django")
        self.testuser1 = User.objects.create_user(
            username="testuser1", password="1234567"
        )
        self.testuser2 = User.objects.create_user(
            username="testuser2", password="1234567"
        )
        test_post = Post.objects.create(
            category_id=1,
            title="Post title",
            excerpt="Post description",
            content="Post description",
            author_id=1,
        )
        client.login(username=self.testuser1.username, password="1234567")

        url = reverse(("blog_api:detailcreate"), kwargs={"pk": 1})

        response = client.put(
            url,
            {
                "title": "Post title",
                "author": 1,
                "excerpt": "Post description",
                "content": "Post description",
            },
            format="json",
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
