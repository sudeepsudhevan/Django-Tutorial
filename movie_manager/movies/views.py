from django.shortcuts import render
from .models import MovieInfo
from .forms import MovieInfoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def create(request):
    form = MovieInfoForm()
    if request.POST:
        # title = request.POST.get("title")
        # year = request.POST["year"]
        # summary = request.POST["summary"]
        # print(title, year, summary)
        form = MovieInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = MovieInfoForm()
    return render(request, "create.html", {"form": form})


@login_required(login_url="login/")
def list(request):
    recent_visits = request.session.get("recent_visits", [])
    count = request.session.get("count", 0)
    # print(type(count))
    count = int(count)
    count = count + 1

    request.session["count"] = count
    recent_movie_set = MovieInfo.objects.filter(pk__in=recent_visits)
    movie_dict = MovieInfo.objects.all().order_by(
        "-year"
    )  # DESC order '-year' for #ASC order 'year'
    # returns a list of all the objects in the database then returns a dictionary with that list as the value of the "movies" key

    response = render(
        request,
        "list.html",
        {"movies": movie_dict, "visits": count, "recent_movies": recent_movie_set},
    )
    return response


@login_required(login_url="login/")
def edit(request, pk):
    instance_to_edit = MovieInfo.objects.get(pk=pk)
    # form = MovieInfoForm(instance=instance)
    if request.POST:
        form = MovieInfoForm(request.POST, request.FILES, instance=instance_to_edit)
        if form.is_valid():
            form.save()
    else:
        recent_visits = request.session.get("recent_visits", [])
        recent_visits.insert(0, pk)
        request.session["recent_visits"] = recent_visits

        form = MovieInfoForm(instance=instance_to_edit)
    return render(request, "edit.html", {"form": form})


@login_required(login_url="login/")
def delete(request, pk):
    instance_to_delete = MovieInfo.objects.get(pk=pk)
    instance_to_delete.delete()

    movie_dict = {"movies": MovieInfo.objects.all()}
    return render(request, "list.html", movie_dict)
