from django.urls import path
from . import views

app_name = 'Destination'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('reg/', views.customer_register, name='reg'),
    path('Destination/reviews/<int:destination_id>/', views.user_reviews.as_view(), name='item_review'),
    path('reviews/', views.view_review, name='user_reviews'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
]
