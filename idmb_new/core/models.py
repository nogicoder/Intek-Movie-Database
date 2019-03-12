from django.db.models import (Model, CharField, TextField, 
DateField, IntegerField, ImageField, BooleanField,
ManyToManyField, ForeignKey, DateTimeField, CASCADE)

class Movie(Model):

    ACTION = 0
    ADVENTURE = 1
    ANIMATION = 2
    BIOGRAPHY = 3
    COMEDY = 4
    THRILLER = 5

    CATEGORIES = ((ACTION, 'action'),
                  (ADVENTURE, 'adventure'),
                  (ANIMATION, 'animation'),
                  (BIOGRAPHY, 'biography'),
                  (COMEDY, 'comedy'),
                  (THRILLER, 'thriller'),)

    title = CharField(max_length=140, blank=False)
    description = TextField(blank=False)
    release_date = DateField(blank=False)
    category = IntegerField(choices=CATEGORIES, blank=False)
    logo = ImageField(blank=True, upload_to='posters', default='posters/noimg.jpg')
    actors = ManyToManyField(
        to='Actor',
        related_name='acting_credits',
        blank=True
    )

    class Meta:
        ordering = ('-release_date', 'title')

    def __str__(self):
        return "{} {}".format(self.title, self.release_date)


class Actor(Model):
    MALE = 0
    FEMALE = 1
    UNSPECIFIED = 2
    
    GENDERS = (
        (MALE, 'male'),
        (FEMALE, 'female'),
        (UNSPECIFIED, 'unspecified'),
    )

    first_name = CharField(max_length=140, blank=False)
    last_name = CharField(max_length=140, blank=False)
    birth_date = DateField(blank=False)
    sex = IntegerField(choices=GENDERS, blank=False)
    nationality = CharField(max_length=140, blank=False)
    alive = BooleanField(null=True)
    avatar = ImageField(blank=True, upload_to='avatars', default='avatars/noimg.jpg')
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Award(Model):
    MOVIE = 0
    ACTOR = 1
    TYPES = (
        (MOVIE, "movie"),
        (ACTOR, "actor"),
    )
    name = CharField(max_length=140, blank=False)
    kind = IntegerField(choices=TYPES, blank=False)
    movie = ForeignKey(Movie, on_delete=CASCADE, blank=True, null=True)
    actor = ForeignKey(Actor, on_delete=CASCADE, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {}".format(self.name, self.kind)