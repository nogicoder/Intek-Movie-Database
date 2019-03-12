from django.db import models

# Create your models here.
class Movie(models.Model):
    ACTION = 0
    ADVENTURE = 1
    ANIMATION = 2
    BIOGRAPHY = 3
    COMEDY = 4
    MOVIE_CATEGORIES = (
                        (ACTION, "Action"), 
                        (ADVENTURE, "Adventure"), 
                        (ANIMATION, "Animation"), 
                        (BIOGRAPHY, "Biography"), 
                        (COMEDY, "Comedy"),
                        )

    title = models.CharField(max_length=140, blank=False)
    description = models.TextField(blank=False)
    release_date = models.DateField(blank=False)
    category = models.IntegerField(choices=MOVIE_CATEGORIES, blank=False)
    logo = models.ImageField(blank=True, null=True, upload_to='logos', default='logos/noimg.jpg')
    
    def __str__(self):
        return "{} {}".format(self.title, self.release_date)


