from django.test import TestCase, Client
from maths.models import Math, Result


class MathViewsTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        self.client = Client()

    def test_maths_list(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<li><a href="/maths/histories/1">id:1, a=20, b=30, op=sub</a></li>', response.content.decode())

    def test_add(self):
        response = self.client.get("/maths/add/1/2")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Wynik operacji 1 + 2 wynosi 3', response.content.decode())

    def test_sub(self):
        response = self.client.get("/maths/sub/1/2")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Wynik operacji 1 - 2 wynosi -1', response.content.decode())

    def test_mul(self):
        response = self.client.get("/maths/mul/2/3")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Wynik operacji 2 * 3 wynosi 6', response.content.decode())

    def test_div(self):
        response = self.client.get("/maths/div/10/2")
        self.assertEqual(response.status_code, 200)
        self.assertIn('Wynik operacji 10 / 2 wynosi 5', response.content.decode())

    def test_maths_details(self):
        response = self.client.get("/maths/histories/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<a href="/maths/histories/">back</a>', response.content.decode())
        
class ResultViewsTest(TestCase):
    
    def setUp(self):
        Result.objects.create(value=180)
        self.client = Client()

    def test_results_list(self):
        response = self.client.get("/maths/results/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<li>value:180.0 | error:None</li>', response.content.decode())
    
class MathViewsPaginationTest(TestCase):
    fixtures = ['math', 'result']

    def setUp(self):
        self.client = Client()

    def test_get_first_5(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 5)

    def test_get_last_page(self):
        response = self.client.get("/maths/histories/?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 2)





