from django.db.models import (Model, CharField, TextField, 
DateField, IntegerField, ImageField)

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

    class Meta:
        ordering = ('-release_date', 'title')

    def __str__(self):
        return "{} {}".format(self.title, self.release_date)
