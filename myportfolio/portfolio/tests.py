from django.test import TestCase
from django.urls import reverse
from .models import Skill, Contact

class ContactViewTests(TestCase):
    def test_contact_view_get(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/contact.html')

    def test_contact_view_post_valid(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message',
        }
        response = self.client.post(reverse('portfolio:contact'), data=form_data)
        self.assertRedirects(response, reverse('portfolio:skills'))
        self.assertTrue(Contact.objects.filter(name='Test User').exists())

    def test_contact_view_post_invalid(self):
        form_data = {}  # Missing required fields
        response = self.client.post(reverse('portfolio:contact'), data=form_data)
        self.assertTemplateUsed(response, 'portfolio/contact.html')
        form = response.context['form']
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')

class SkillsViewTests(TestCase):
    def test_skills_view(self):
        Skill.objects.create(name='Test Skill')
        response = self.client.get(reverse('portfolio:skills'))
        self.assertTemplateUsed(response, 'portfolio/skills.html')
        self.assertContains(response, 'Test Skill')
