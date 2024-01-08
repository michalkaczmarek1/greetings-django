from django.test import TestCase
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm


class PostFormTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="michal88", email="test@test.com")
        
    def test_post_save_correct_data(self):
        data = {
            "title": "test",
            "content": "lorem ipsum",
            "author": Author.objects.get(nick="michal88")
        }
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        p = form.save()
        self.assertIsInstance(p, Post)
        self.assertEqual(p.content, "lorem ipsum")
        self.assertIsNotNone(p.id)

class AuthorFormTest(TestCase):

    def test_author_save_correct_data(self):
        data = {
            "nick": "test",
            "email": "test@test.com",
            "bio": "test"
        }
        self.assertEqual(len(Author.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        a = form.save()
        self.assertIsInstance(a, Author)
        self.assertEqual(a.nick, "test")
        self.assertIsNotNone(a.id)