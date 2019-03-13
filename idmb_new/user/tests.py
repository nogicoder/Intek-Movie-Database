from core.models import Movie, Category
from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """
    Test for status code and correct template mapping
    of the Homepage using SimpleTestCase.
    """

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


class MovieViewTests(TestCase):
    "Test for correct Object creation."

    def setUp(self):
        """
        Setting up the Test, pre-populating the database
        with 2 objects: A Category instance and a Movie instance.
        """
        Category.objects.create(category='Action')
        Movie.objects.create(title='Test',
                             description='Testing',
                             release_date='2019-01-08',
                             category=Category.objects.get(id=1))

    def test_movie_content(self):
        """
        Test the validity of the data passed into the database
        with all fields, including both required and optional 
        fields.
        """
        movie = Movie.objects.get(id=1)
        expected_object_title = f'{movie.title}'
        expected_object_description = f'{movie.description}'
        expected_object_release_date = f'{movie.release_date}'
        expected_object_category = f'{movie.category}'
        expected_object_actors = f'{movie.actors}'
        self.assertEquals(expected_object_title, 'Test')
        self.assertEquals(expected_object_description, 'Testing')
        self.assertEquals(expected_object_release_date, '2019-01-08')
        self.assertEquals(expected_object_category, 'Action')
        self.assertEquals(expected_object_actors, 'core.Actor.None')

    def test_movie_detail_view(self):
        """
        Test the status code, object reference and right template
        used to get user's data.
        """
        response = self.client.get(reverse('core:moviedetail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')
        self.assertTemplateUsed(response, 'core/movie_detail.html')

    def test_movie_update_view(self):
        """
        Test the status code, object reference and right template
        used to update user's data.
        """
        update_url = reverse('core:movieupdate', args=[1])
        r = self.client.get(update_url)
        form = r.context['form']
        data = form.initial
        data['title'] = 'Changed'
        response = self.client.post(update_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Movie.objects.get(pk=1).title, 'Changed')

    def test_movie_delete_view(self):
        """
        Test the status code, object reference and right template
        used to delete user's data.
        """
        response = self.client.post(reverse('core:moviedelete', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(list(Movie.objects.all()), [])


class ActorViewTests(TestCase):
    "Test for correct Object creation."

    def setUp(self):
        """
        Setting up the Test, pre-populating the database
        with 3 objects: A Category instance, a Movie instance
        and an Actor instance.
        """
        Category.objects.create(category='Action')
        Movie.objects.create(title='Test',
                             description='Testing',
                             release_date='2019-01-08',
                             category=Category.objects.get(id=1))
        Actor.objects.create()

    def test_movie_content(self):
        """
        Test the validity of the data passed into the database
        with all fields, including both required and optional 
        fields.
        """
        movie = Movie.objects.get(id=1)
        expected_object_title = f'{movie.title}'
        expected_object_description = f'{movie.description}'
        expected_object_release_date = f'{movie.release_date}'
        expected_object_category = f'{movie.category}'
        expected_object_actors = f'{movie.actors}'
        self.assertEquals(expected_object_title, 'Test')
        self.assertEquals(expected_object_description, 'Testing')
        self.assertEquals(expected_object_release_date, '2019-01-08')
        self.assertEquals(expected_object_category, 'Action')
        self.assertEquals(expected_object_actors, 'core.Actor.None')

    def test_movie_detail_view(self):
        """
        Test the status code, object reference and right template
        used to get user's data.
        """
        response = self.client.get(reverse('core:moviedetail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')
        self.assertTemplateUsed(response, 'core/movie_detail.html')

    def test_movie_update_view(self):
        """
        Test the status code, object reference and right template
        used to update user's data.
        """
        update_url = reverse('core:movieupdate', args=[1])
        r = self.client.get(update_url)
        form = r.context['form']
        data = form.initial
        data['title'] = 'Changed'
        response = self.client.post(update_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Movie.objects.get(pk=1).title, 'Changed')

    def test_movie_delete_view(self):
        """
        Test the status code, object reference and right template
        used to delete user's data.
        """
        response = self.client.post(reverse('core:moviedelete', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(list(Movie.objects.all()), [])
