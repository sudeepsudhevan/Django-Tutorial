from django.forms import ModelForm
from .models import MovieInfo


class MovieInfoForm(ModelForm):
    class Meta:
        model = MovieInfo
        fields = "__all__"
