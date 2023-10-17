from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm,ProfileForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth import login ,authenticate
# Create your views here.

class RegisterView(generic.CreateView):
	form_class = SignupForm
	success_url= reverse_lazy('home')
	template_name = "registration/register.html"
	def form_valid(self, form):
		valid = super(RegisterView, self).form_valid(form)
		username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return valid



class Profile(UpdateView):
	model = User
	form_class = ProfileForm
	template_name = 'registration/profile.html'
	success_url = reverse_lazy('profile')
	def get_object(self):
		return User.objects.get(pk=self.request.user.pk)

class Login(LoginView):
	    def get_success_url(self):
	    	return reverse_lazy('home') 
class PasswordChange(PasswordChangeView):
	success_url = reverse_lazy('home')