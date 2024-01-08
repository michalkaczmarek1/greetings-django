from django.test import TestCase, Client


class GreetingsViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_greetings(self):
        response = self.client.get("/greetings/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello World!', response.content.decode())

    def test_greetings_with_name(self):
        response = self.client.get("/greetings/michal")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello Michal', response.content.decode())