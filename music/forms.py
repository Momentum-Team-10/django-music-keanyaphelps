from django import forms
from .models import Album


# define class AlbumForm(forms.ModelForm)
# inside of this class define class Meta
# define model that AlbumForm is connected to
# define a list called fields whose values are the fields from Album model, and values should be strings 
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "artist", "created_at"]