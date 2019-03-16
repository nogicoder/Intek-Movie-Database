from django.db.models import (Model, CharField, TextField,
                              DateField, IntegerField, ImageField, BooleanField,
                              ManyToManyField, ForeignKey, DateTimeField, CASCADE)


class Category(Model):
    """
    Initiate the Model for Category object.
    """

    category = CharField(max_length=140, blank=False, unique=True)

    def __str__(self):
        return self.category


class Movie(Model):
    """
    Initiate the Model for Movie object.
    """

    title = CharField(max_length=140, blank=False)
    description = TextField(blank=False)
    release_date = DateField(blank=False)
    category = ForeignKey(Category, on_delete=CASCADE, blank=False, null=True)
    logo = ImageField(blank=True, upload_to='posters',
                      default='posters/noimg.jpg')

    # Using the manytomany model to map Actor table and Movie table in the database
    actors = ManyToManyField(
        to='Actor',
        related_name='acting_credits',
        blank=True)

    # Order the list by date and title
    class Meta:
        ordering = ('-release_date', 'title')

    # Displaying the name of the object
    def __str__(self):
        return self.title


class Actor(Model):
    """
    Initiate the Model for Actor object.
    """

    MALE = 0
    FEMALE = 1
    UNSPECIFIED = 2

    GENDERS = (
        (MALE, 'male'),
        (FEMALE, 'female'),
        (UNSPECIFIED, 'unspecified'))

    first_name = CharField(max_length=140, blank=False)
    last_name = CharField(max_length=140, blank=False)
    birth_date = DateField(blank=False)
    sex = IntegerField(choices=GENDERS, blank=False)
    nationality = CharField(max_length=140, blank=False)
    alive = BooleanField(null=True)
    avatar = ImageField(blank=True, upload_to='avatars',
                        default='avatars/noimg.jpg')

    # Displaying the name of the object
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Award(Model):
    """
    Initiate the Model for Award object.
    """

    MOVIE = 0
    ACTOR = 1
    TYPES = (
        (MOVIE, "movie"),
        (ACTOR, "actor"),
    )
    name = CharField(max_length=140, blank=False)
    kind = IntegerField(choices=TYPES, blank=False)
    movie = ManyToManyField(
        to='Movie',
        related_name='movie_credits',
        blank=True)
    actor = ManyToManyField(
        to='Actor',
        related_name='actor_credits',
        blank=True)
    created_at = DateField(blank=False)

    # Displaying the name of the object
    def __str__(self):
        return "{} - {}".format(self.name, self.kind)


class MovieComment(Model):
    """
    Initiate the Model for Movie Commenting.
    """

    # Setting the OnetoMany relationship between Movie and MovieComment object in the database
    movie = ForeignKey(Movie, on_delete=CASCADE, related_name='comments')
    author = CharField(max_length=200)
    text = TextField()
    created_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class ActorComment(Model):
    """
    Initiate the Model for Actor Commenting.
    """

    # Setting the OnetoMany relationship between Actor and ActorComment object in the database
    actor = ForeignKey(Actor, on_delete=CASCADE, related_name='comments')
    author = CharField(max_length=200)
    text = TextField()
    created_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class AwardComment(Model):
    """
    Initiate the Model for Award Commenting.
    """

    # Setting the OnetoMany relationship between Award and AwardComment object in the database
    award = ForeignKey(Award, on_delete=CASCADE, related_name='comments')
    author = CharField(max_length=200)
    text = TextField()
    created_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
