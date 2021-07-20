from django.urls import path

from accountapp.views import hello_1ban, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_1ban/', hello_1ban, name='hello_1ban'),

    path('create/', AccountCreateView.as_view(), name='create'),
]