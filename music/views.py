from django.shortcuts import render
from .models import Album

# Create your views here.
# define a view that will list all albums in database
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "list_albums.html", {"albums": albums})
# define a view that will let us create a new album
# define a view that will give details for specific album by ID
# define a view that will allow us to edit album
# define a view that will allow us to delete album
