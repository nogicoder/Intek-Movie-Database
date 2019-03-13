from core.models import Category, Movie, Actor, Award
from django.test import TestCase
from django.urls import reverse


class MoviePageTests(TestCase):
    """
    Test for status code and correct template mapping
    of the Movie page.
    """

    def test_movie_page_status_code(self):
        response = self.client.get(reverse('core:movielist'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('core:movielist'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/movie_list.html')


class ActorPageTests(TestCase):
    """
    Test for status code and correct template mapping
    of the Actor page.
    """

    def test_actor_page_status_code(self):
        response = self.client.get(reverse('core:actorlist'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('core:actorlist'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/actor_list.html')


class AwardPageTests(TestCase):
    """
    Test for status code and correct template mapping
    of the Award page.
    """

    def test_award_page_status_code(self):
        response = self.client.get(reverse('core:awardlist'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('core:awardlist'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/award_list.html')


class CategoryModelTests(TestCase):
    """Model Creation Test for Category"""

    def setUp(self):
        """
        Setting up the Test, pre-populating the database
        with 2 objects: A Category instance and a Movie instance.
        """
        Category.objects.create(category='Action')

    def test_movie_model(self):
        """
        Test the validity of the data passed into the database
        with all fields, including both required and optional 
        fields.
        """
        category = Category.objects.get(id=1)
        expected_object_name = f'{category.category}'
        self.assertEquals(expected_object_name, 'Action')


class MovieModelTests(TestCase):
    """Model Creation Test for Movie"""

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

    def test_movie_model(self):
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

    def test_movie_unhappy(self):
        """
        Test when field input is invalid.
        """
        update_url = reverse('core:movieupdate', args=[1])
        r = self.client.get(update_url)
        form = r.context['form']
        data = form.initial
        data['category'] = 'Changed'
        response = self.client.post(update_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Movie.objects.get(pk=1).category == 'Changed')


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

    def test_movie_unhappy(self):
        """
        Test the status code after delete user's data.
        """
        r = self.client.post(reverse('core:moviedelete', args=[1]))
        response = self.client.get(reverse('core:moviedetail', args=[1]))
        self.assertEqual(response.status_code, 404)



class ActorModelTests(TestCase):
    """Model Creation Test for Actor"""

    def setUp(self):
        """
        Setting up the Test, pre-populating the database
        with 3 objects: A Category instance, a Movie instance
        and an Actor instance.
        """
        Category.objects.create(category='Action')
        actor = Actor.objects.create(first_name="First",
                                     last_name="Last",
                                     birth_date="2019-08-02",
                                     sex=0,
                                     nationality='Vietnam'
                                     )
        movie = Movie.objects.create(title='Test',
                                     description='Testing',
                                     release_date='2019-01-08',
                                     category=Category.objects.get(id=1))
        movie.actors.add(actor)

    def test_actor_model(self):
        """
        Test the validity of the data passed into the database
        with all fields, including both required and optional 
        fields.
        """
        actor = Actor.objects.get(id=1)
        expected_object_first = f'{actor.first_name}'
        expected_object_last = f'{actor.last_name}'
        expected_object_birth_date = f'{actor.birth_date}'
        expected_object_sex = f'{actor.sex}'
        expected_object_nationality = f'{actor.nationality}'
        self.assertEquals(expected_object_first, 'First')
        self.assertEquals(expected_object_last, 'Last')
        self.assertEquals(expected_object_birth_date, '2019-08-02')
        self.assertEquals(expected_object_sex, '0')
        self.assertEquals(expected_object_nationality, 'Vietnam')


class ActorViewTests(TestCase):
    "Test for correct Object creation."

    def setUp(self):
        """
        Setting up the Test, pre-populating the database
        with 3 objects: A Category instance, a Movie instance
        and an Actor instance.
        """
        Category.objects.create(category='Action')
        actor = Actor.objects.create(first_name="First",
                                     last_name="Last",
                                     birth_date="2019-08-02",
                                     sex=0,
                                     nationality='Vietnam'
                                     )
        movie = Movie.objects.create(title='Test',
                                     description='Testing',
                                     release_date='2019-01-08',
                                     category=Category.objects.get(id=1))
        movie.actors.add(actor)

    def test_actor_detail_view(self):
        """
        Test the status code, object reference and right template
        used to get user's data.
        """
        response = self.client.get(reverse('core:actordetail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Last')
        self.assertTemplateUsed(response, 'core/actor_detail.html')

    def test_actor_update_view(self):
        """
        Test the status code, object reference and right template
        used to update user's data.
        """
        update_url = reverse('core:actorupdate', args=[1])
        r = self.client.get(update_url)
        form = r.context['form']
        data = form.initial
        data['first_name'] = 'Changed'
        response = self.client.post(update_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Actor.objects.get(pk=1).first_name, 'Changed')

    def test_actor_delete_view(self):
        """
        Test the status code, object reference and right template
        used to delete user's data.
        """
        response = self.client.post(reverse('core:actordelete', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(list(Actor.objects.all()), [])

    def test_actor_unhappy(self):
        """
        Test the status code after delete user's data.
        """
        r = self.client.post(reverse('core:actordelete', args=[1]))
        response = self.client.get(reverse('core:actordetail', args=[1]))
        self.assertEqual(response.status_code, 404)


class AwardModelTests(TestCase):
    """Model Creation Test for Award"""

    def setUp(self):
        """
        Setting up the Test, pre-populating the database
        with 4 objects: A Category instance, a Movie instance, 
        an Actor instance and an Award instance.
        """
        Category.objects.create(category='Action')
        actor = Actor.objects.create(first_name="First",
                                     last_name="Last",
                                     birth_date="2019-08-02",
                                     sex=0,
                                     nationality='Vietnam')
        movie = Movie.objects.create(title='Test',
                                     description='Testing',
                                     release_date='2019-01-08',
                                     category=Category.objects.get(id=1))
        award = Award.objects.create(name="Oscar",
                                     kind=0,
                                     movie=movie,
                                     actor=actor)

    def test_award_model(self):
        """
        Test the validity of the data passed into the database
        with all fields, including both required and optional 
        fields.
        """
        award = Award.objects.get(id=1)
        expected_object_name = f'{award.name}'
        expected_object_kind = f'{award.kind}'
        expected_object_movie = f'{award.movie}'
        expected_object_actor = f'{award.actor}'
        expected_object_time = f'{award.created_at}'
        self.assertEquals(expected_object_name, 'Oscar')
        self.assertEquals(expected_object_kind, '0')
        self.assertEquals(expected_object_movie, 'Test')
        self.assertEquals(expected_object_actor, 'First Last')


class AwardViewTests(TestCase):
    "Test for correct Object creation."

    def setUp(self):
        """
        Setting up the Test, pre-populating the database
        with 4 objects: A Category instance, a Movie instance, 
        an Actor instance and an Award instance.
        """
        Category.objects.create(category='Action')
        actor = Actor.objects.create(first_name="First",
                                     last_name="Last",
                                     birth_date="2019-08-02",
                                     sex=0,
                                     nationality='Vietnam')
        movie = Movie.objects.create(title='Test',
                                     description='Testing',
                                     release_date='2019-01-08',
                                     category=Category.objects.get(id=1))
        award = Award.objects.create(name="Oscar",
                                     kind=0,
                                     movie=movie,
                                     actor=actor)

    def test_award_detail_view(self):
        """
        Test the status code, object reference and right template
        used to get user's data.
        """
        response = self.client.get(reverse('core:awarddetail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Oscar')
        self.assertTemplateUsed(response, 'core/award_detail.html')

    def test_award_update_view(self):
        """
        Test the status code, object reference and right template
        used to update user's data.
        """
        update_url = reverse('core:awardupdate', args=[1])
        r = self.client.get(update_url)
        form = r.context['form']
        data = form.initial
        data['name'] = 'Changed'
        response = self.client.post(update_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Award.objects.get(pk=1).name, 'Changed')

    def test_award_delete_view(self):
        """
        Test the status code, object reference and right template
        used to delete user's data.
        """
        response = self.client.post(reverse('core:awarddelete', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(list(Award.objects.all()), [])

    def test_award_unhappy(self):
        """
        Test the status code after delete user's data.
        """
        r = self.client.post(reverse('core:awarddelete', args=[1]))
        response = self.client.get(reverse('core:awarddetail', args=[1]))
        self.assertEqual(response.status_code, 404)
