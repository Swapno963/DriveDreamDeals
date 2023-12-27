from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages

# function besed view
from django.contrib.auth import logout
# class besed vew
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# FOR Profile
from car.models import CarModel
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Register Successfull!')
            # return redirect()

    else:
        register_form = forms.RegistrationForm()
    return render(request,'register.html',{'form':register_form,'type':'Register'})
            

class UserLoginView(LoginView):
    template_name = 'register.html'
    success_url = reverse_lazy('/motorists/profile')

    def form_valid(self,form):
        messages.success(self.request, 'Login Successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Login Information Incorrect!')
        return super().form_invalid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

def show_profile(request):
    # data = CarModel.objects.filter(brand = request.user)
    data = CarModel.objects.all()
    return render(request, 'show_profile.html',{'data':data})

def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile Updated Successfully!')
    
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, 'update_profile.html', {'form':profile_form})
