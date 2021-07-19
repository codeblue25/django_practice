from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import User


def hello_1ban(request):

    if request.method == 'POST':

        temp = request.POST.get('user_id')

        new_user = User()
        new_user.text = temp
        new_user.save()

        return render(request, 'accountapp/hello_1ban.html', context={'user_output': new_user})
    else:
        return render(request, 'accountapp/hello_1ban.html', context={'text': 'GET METHOD!!'})
