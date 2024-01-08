from django.test import TestCase
from posts.models import Post, Author


class PostModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="michal88", email="test@test.com")
        Post.objects.create(title="test1", content="lorem ipsum", author=Author.objects.get(nick="michal88"))
        Post.objects.create(title="test2", content="lorem ipsum2", author=Author.objects.get(nick="michal88"))
        

    def test_post_str(self):
        p1 = Post.objects.get(title="test1")
        p2 = Post.objects.get(title="test2")

        self.assertEqual(str(p1), "title:test1, autor:nick:michal88 | email:test@test.com")
        self.assertEqual(str(p2), "title:test2, autor:nick:michal88 | email:test@test.com")

class AutorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="test22", email="test@gmail.com")
        Author.objects.create(nick="test33", email="test3@gmail.com")

    def test_author_str(self):
        a1 = Author.objects.get(nick="test22")
        a2 = Author.objects.get(nick="test33")

        self.assertEqual(str(a1), 'nick:test22 | email:test@gmail.com')
        self.assertEqual(str(a2), 'nick:test33 | email:test3@gmail.com')