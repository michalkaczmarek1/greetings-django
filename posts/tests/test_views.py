from django.test import TestCase, Client
from posts.models import Post, Author


class PostViewsTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="michal88", email="test@test.com")
        Post.objects.create(title="test1", content="lorem ipsum", author=Author.objects.get(nick="michal88"))
        Post.objects.create(title="test2", content="lorem ipsum2", author=Author.objects.get(nick="michal88"))
        self.client = Client()

    def test_posts_list(self):
        response = self.client.get("/posts/list/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<a href="/posts/post/1">title:test1, autor:nick:michal88 | email:test@test.com</a>', response.content.decode())

    def test_post_details(self):
        response = self.client.get("/posts/post/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<a href="/posts/list/">back</a>', response.content.decode())

    

class AuthorViewsTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="michal88", email="test@test.com")
        self.client = Client()

    def test_authors_list(self):
        response = self.client.get("/posts/authors/list/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<a href="/posts/author/1">nick:michal88 | email:test@test.com</a>', response.content.decode())

    def test_author_details(self):
        response = self.client.get("/posts/author/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<a href="/posts/authors/list/">back</a>', response.content.decode())




    