from django.shortcuts import redirect, render
from movies.forms import MoviesForm
from movies.models import Movies


# Create your views here.
def index(request):

  movies = Movies.objects.all()

  context = {
    'movies' : movies,
  }

  return render(request, 'movies/index.html', context)

def create(request):

  if request.method == 'POST':
      movies_form = MoviesForm(request.POST)
      if movies_form.is_valid():
        movies_form.save()
        return redirect("movies:index")
  else:
    movies_form = MoviesForm()

  context = {
    'movies_form' : movies_form,
  }  
  return render(request, 'movies/create.html', context)

def detail(request, pk):

  movie = Movies.objects.get(pk=pk)

  context = {
    'movie' : movie,
  }


  return render(request, 'movies/detail.html', context)


def update(request, pk):

  movie = Movies.objects.get(pk=pk)
  if request.method == 'POST':
    movie_form = MoviesForm(request.POST, instance=movie)
    if movie_form.is_valid():
      movie_form.save()
      return redirect('movies:detail', movie.pk)
  else:
    movie_form = MoviesForm(instance=movie)
  context = {
    'movies_form' : movie_form,
  }

  return render(request, 'movies/update.html', context)

# get으로 구현
def delete(request, pk):

  movies = Movies.objects.get(pk=pk)
  movies.delete()

  return redirect('movies:index')