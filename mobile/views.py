from django.shortcuts import render
from .forms import Form
from django.views.generic.base import TemplateView

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


class About(TemplateView):
    template_name = 'home.html'


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
