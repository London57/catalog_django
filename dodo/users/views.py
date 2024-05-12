from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationUserForm, LoginUserForm
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
# from django.views.generic import



def myprofile(request):
    return render(request, template_name='my_profile.html')

    
class RegistrationView(View):
    def get(self, request):
        context = {'form': RegistrationUserForm}
        return render(request, template_name='registration.html', context=context)
    
    def post(self, request):
        form = RegistrationUserForm(request.POST)
        
        if form.is_valid():
            # form.instance.password = form.clean_password2()
            # form.save(commit=False)
            # print(form)
            # form.cleaned_data['password'] = form.clean_password2()
            form.save()
            return redirect('login')
        return render(request, 'registration.html', context={'form': RegistrationUserForm,
                                                              'errors':form.errors})
    

    
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form': LoginUserForm})
    
    def post(self, request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            user = authenticate(request, username=data['username'],
                                password=data['password'],)
            if user:
                login(request, user)
                return redirect('my_profile')
            return render(request, 'login.html', {'form': LoginUserForm, 'errors': 'Invalid username or password'})
        
        return render(request, 'login.html', {'form': LoginUserForm, 'other_errors':form.errors})