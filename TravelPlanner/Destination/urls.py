from django.urls import path
from . import views
app_name = 'Destination'

urlpatterns = [

    path('', views.HomeView.as_view(), name='index'),
    path('reg', views.customer_register, name='reg'),
]
