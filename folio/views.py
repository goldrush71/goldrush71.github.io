from django.shortcuts import render, HttpResponse

# Create your views here.


def home_page_view(request):
    return render(request, "home.html")
