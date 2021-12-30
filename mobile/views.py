from django.shortcuts import render
from .forms import Form
from django.views.generic.base import TemplateView
from mobile.serializers import PostSerializers
from rest_framework import generics
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Mobile
# Create your views here.


def home_view(request):
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
        else:
            form = Form()
            return render(request, 'index.html', {'form': form})

    return render(request, 'index.html', {'form': form})


class EmployeeUpdate(UpdateView):
    model = Mobile
    fields = '__all__'
    template_name = "update.html"

    def get_success_url(self):
        return reverse('home')


class home(TemplateView):
    template_name = 'ROOT.html'


'''
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
        else:
            form = Form()
            return render(request, 'index.html', {'form': form})
    stu = Form()
    return render(request, "index.html", {'form': form})
'''
