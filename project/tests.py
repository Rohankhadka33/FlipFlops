from django.contrib.auth.models import User
from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve
from project.models import Register
from project.views import login, index, logout, shoes, deleteproduct, adminpanel, deleteorder


# Create your tests here.
class TestUrls(SimpleTestCase):
    # Home page Testing, and It is Customer/User and Admin Signin Testing as well
    def test_case_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

        # Create Contact Us Testing

    def test_case_signin_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

        # Create Contact Us Testing

    def test_case_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_case_logout_url(self):
        url = reverse('adminpanel')
        self.assertEquals(resolve(url).func, adminpanel)

        # Delete Contact Us Testing

    def test_case_delete_url(self):
        url = reverse('deleteproducts', args=[1])
        self.assertEquals(resolve(url).func, deleteproduct)

        # Creating Signup or Customer registration Testing

    def test_case_deleteorder_url(self):
        url = reverse('deleteorder', args=[1])
        self.assertEquals(resolve(url).func, deleteorder)

        # Delete Registered Customer Testing


class TestViews(TestCase):
    # Testing User Authentication in home view
    def test_case_home_views(self):
        user = User.objects.create(username='testcase')
        user.set_password('12434345')
        user.save()
        client = Client()
        logged_in = client.login(username='testcase', password="12434345")
        url = reverse('login')
        response = client.get(url)
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        # Testing Contact Create in Contact us view

    def test_case_CreateContact_views(self):
        client = Client()
        url = reverse('register')
        response = client.post(url, {
            'name': 'name',
            'email': 'email',
            'password': 'password',
        })

        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        # Testing Contact Delete in Contact us view

    def test_case_DeleteContact_views(self):
        client = Client()

        newlycreated = Register.objects.create(
            {
                'name': 'name',
                'email': 'email',
                'password': 'password',
            })
        print(newlycreated.id)
        url = reverse('deleteusers', newlycreated.id)
        response = client.delete(url)

        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertRedirects(response, '/adminpanel')
