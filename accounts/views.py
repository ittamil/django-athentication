from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm , EditProfileForm

def index(request):
    return render(request,'index.html')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(request.POST,instance = request.user)
    context = {
        'form':form
    }   
    return render(request,'edit_profile.html',context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=RegistrationForm()
    context = {
        'form':form
    }    
    return render(request,'registration/register.html',context)

def error404(request,exception):
    return render(request,'404.html')



