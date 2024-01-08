from unittest import TestCase
from django.urls import resolve
from posts.views import post_details, author_details, posts_list, authors_list


class TestUrls(TestCase):
    def test_resolution_for_posts_list(self):
        resolver = resolve('/posts/list/')
        self.assertEqual(resolver.func, posts_list)

    def test_resolution_for_post_details(self):
        resolver = resolve('/posts/post/1')
        self.assertEqual(resolver.func, post_details)

    def test_resolution_for_authors_list(self):
        resolver = resolve('/posts/authors/list/')
        self.assertEqual(resolver.func, authors_list)

    def test_resolution_for_author_details(self):
        resolver = resolve('/posts/author/1')
        self.assertEqual(resolver.func, author_details)


