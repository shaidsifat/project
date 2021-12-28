from django.shortcuts import render
from .forms import Form

# Create your views here.


def home_view(request):

    stu = Form()
    return render(request, "index.html", {'form': stu})
