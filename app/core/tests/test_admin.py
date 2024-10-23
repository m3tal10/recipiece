from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='mashrafie@dev.to',
            password='test1234')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='mashrafie@gmail.com',
            password='test1234',
            name='mash')

    def test_for_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name.lower())
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that user edit page works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # the url is going to look like this admin/core/user/<user.id>/change
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def create_user_page(self):
        """Test that user create page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
