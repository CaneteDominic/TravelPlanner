from django.shortcuts import render
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

    return render(request, 'index.html', {'form': form})


class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        form = DestinationRegister()
        return render(request, self.template_name, {'form': form})
