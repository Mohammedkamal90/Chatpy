from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Message, Group

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
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('index'))  

        user = User.objects.filter(username='newuser').first()
        self.assertIsNotNone(user)

class MessageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.group = Group.objects.create(name='Test Group')

    def test_message_creation(self):
        message = Message.objects.create(content='Test Message', user=self.user, group=self.group)
        self.assertEqual(message.content, 'Test Message')
        self.assertEqual(message.user.username, 'testuser')
        self.assertEqual(message.group.name, 'Test Group')
