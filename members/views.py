"""
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm    
    template_name = "registration/register.html"
    success_url = reverse_lazy('entity')"""
    
from django.shortcuts import render, redirect
from members.forms import UserAdminCreationForm
from django.urls import reverse_lazy

def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(req, 'registration/register.html', {'form': form})
  