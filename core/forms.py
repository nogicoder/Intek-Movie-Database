from django.forms import ModelForm, DateField, SelectDateWidget
from .models import Movie, Actor, Award, MovieComment, ActorComment, AwardComment


class MovieForm(ModelForm):
    release_date = DateField(required=True, widget=SelectDateWidget(years=range(1900, 2019)))

    class Meta:
        model = Movie
        fields = "__all__"


class ActorForm(ModelForm):
    birth_date = DateField(required=True, widget=SelectDateWidget(years=range(1900, 2019)))

    class Meta:
        model = Actor
        fields = "__all__"


class AwardForm(ModelForm):
    created_at = DateField(widget=SelectDateWidget(years=range(1900, 2019)))
    class Meta:
        model = Award
        fields = "__all__"


class MovieCommentForm(ModelForm):

    class Meta:
        model = MovieComment
        fields = ('text',)


class ActorCommentForm(ModelForm):

    class Meta:
        model = ActorComment
        fields = ('text',)


class AwardCommentForm(ModelForm):

    class Meta:
        model = AwardComment
        fields = ('text',)
