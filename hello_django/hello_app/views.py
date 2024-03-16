from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def print_hello(request):
    movie_list = {
        "movies": [
            {
                "title": "The Matrix",
                "year": "1999",
                "summary": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                "success": True,
            },
            {
                "title": "The Matrix Reloaded",
                "year": "2003",
                "summary": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                "success": True,
            },
            {
                "title": "The Matrix Revolutions",
                "year": "2003",
                "success": False,
            },
        ]
    }
    return render(request, "hello.html", movie_list)
