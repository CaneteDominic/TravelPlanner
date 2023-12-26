from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.db import connection
from .forms import AddReview, DestinationRegister, LoginForm, Review,UserForm

# Create your views here.
from django.views.generic.base import View


def index(request):
    if request.method == 'POST':
        form = DestinationRegister(request.POST)
        if form.is_valid():
            return HttpResponse("Form submitted successfully.")
    else:
        form = DestinationRegister()

    return render(request, 'destination.html', {'form': index.html})


class HomeView(View):
    template_name = "destination.html"

    def get(self, request):
        form = DestinationRegister()
        return render(request, self.template_name, {'form': form})


def customer_register(request):
    try:
        u = request.session['username']
    except:
        return HttpResponseRedirect('/Destination/login/')
    destinations = Destinations.objects.all()
    return render(request, 'destination.html', {'destinations': destinations})


class UserRegister(View):
    template = 'register.html'

    def get(self, request):
        form = UserForm()
        request.session.clear()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            dob = form.cleaned_data['date_of_birth']
            cnum = form.cleaned_data['contact_number']

            cursor = connection.cursor()
            cursor.callproc('RegisterUser', [username, email, password, firstname, lastname, dob, cnum])
            result = cursor.fetchall()
            cursor.close()

            if result[0][0] > 0:
                form.add_error(None, "User already exists")
            else:
                request.session['username'] = username
                return HttpResponseRedirect('/Destination/reg/')

            return render(request, self.template, {'form': form})


class user_reviews(View):
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, 'reviews.html', {'reviews': reviews})

    def post(self, request):
        username = request.POST.get('username')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        print(username, rating, comment)

        add_review_view = AddReviews()
        if username and rating and comment:
            add_review_view.add_review(username, rating, comment)
            return HttpResponseRedirect('/Destination/view_reviews/')

class AddReviews(View):
    template = 'reviews.html'

    def add_review(self, username, rating, comment):
        if username and rating and comment:
            with connection.cursor() as cursor:
                cursor.callproc('add_review', (username, rating, comment))
                cursor.close()

    def get(self, request):
        form = AddReview()
        return render(request, self.template, {'form': form})


class Login(View):
    template = 'LoginUser.html'

    def get(self, request):
        form = LoginForm()
        request.session.clear()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            cursor = connection.cursor()
            cursor.callproc('LoginUser', [username, password])
            result = cursor.fetchall()
            cursor.close()

            if result[0][0] > 0:
                request.session['username'] = username
                return HttpResponseRedirect('/Destination/reg/')
            else:
                form.add_error(None, "User does not exist")

            return render(request, self.template, {'form': form})


def view_review(request):
    reviews = Review.objects.all()
    return render(request, 'viewreviews.html', {'reviews': reviews})


