from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import User


def hello_1ban(request):

    if request.method == 'POST':

        temp = request.POST.get('user_id')

        new_user = User()
        new_user.text = temp
        new_user.save()

        user_list = User.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_1ban'))
    else:
        user_list = User.objects.all()
        return render(request, 'accountapp/hello_1ban.html', context={'user_list': user_list})