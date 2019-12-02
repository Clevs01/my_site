from django.shortcuts import render
from .models import Learning, AboutMe
from .forms import ContactForm
# from django.contrib import messages

# Create your views here.

# Define the landing page.


def about_tuts(request):
    return render(request, 'tutorials/about.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    abouts = AboutMe.objects.all()
    return render(request, 'about.html', {'abouts': abouts})


def resources(request):
    context = Learning.objects.all()
    return render(request, 'resource.html', {'context': context})


def contact(request):
    if request.method == 'POST':
        # POST, get the data from the form
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # if is valid, just save, and return a new page with thanks
            form.save()
            return render(request, 'thanks.html')
        else:
            # Form has errors, re-render with data and error messages
            return render(request, 'contact.html', {'form': form, })
    else:
        # GET, render new empty form
        form = ContactForm()
        return render(request, 'contact.html', {'form': form, })


def thanks(request):
    return render(request, 'thanks.html')


def exercises(request):
    return render(request, 'tutorials/exercises.html')
