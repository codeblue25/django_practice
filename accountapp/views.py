from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

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

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_1ban')
    template_name = 'accountapp/create.html'