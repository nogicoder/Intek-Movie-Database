from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth.models import User


class MoviePageTests(SimpleTestCase):
    """
    Test for status code and correct template mapping
    of the HomePage.
    """

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/home.html')


class RegistrationViewTests(TestCase):
    """
    Test for status code and correct template mapping
    of the HomePage.
    """

    def setUp(self):
        user = User.objects.create(username='test')
        user.set_password('12345')
        user.save()

    def test_login_logout(self):
        """
        Test when field input is valid.
        Both Login Logout return success status code.
        """
        logged_in = self.client.login(username='test', password='12345')
        self.assertTrue(logged_in)
        logged_out = self.client.logout()
        self.assertIsNone(logged_out)

    def test_login_unhappy(self):
        """
        Test when field input is valid.
        """
        logged_in = self.client.login(username='test', password='')
        self.assertFalse(logged_in)
