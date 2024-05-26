# chat/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class MainPagesTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Chatpy")

class UserAccountTests(TestCase):
    def test_registration_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, reverse('index'))  # Should redirect to 'index' after registration

        # Check that the user is actually created
        user = User.objects.get(username='newuser')
        self.assertIsNotNone(user)
