from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DestinationRegister

# Create your views here.
from django.views.generic.base import View


def index(request):
    if request.method == 'POST':
        form = DestinationRegister(request.POST)
        if form.is_valid():
            return HttpResponse("Form submitted successfully.")
    else:
        form = DestinationRegister()

    return render(request, 'index.html', {'form': index.html})


class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        form = DestinationRegister()
        return render(request, self.template_name, {'form': form})


def customer_register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = DestinationRegister()
    else:
        # Process completed form.
        form = DestinationRegister(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Location Added successfully!")
    context = {'form': form}
    return render(request, 'index.html', context)
