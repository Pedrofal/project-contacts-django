from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
def register(request):
    form = RegisterForm()
    
    
    if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form = form.save()
                messages.success(request, 'User has been registered')
                return redirect('contact:index',)
    return render(
        request, 'contact/register.html',
        {'form': form}
        )
    
def login_view(request):
    
    form = AuthenticationForm()
    if  request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, f'Login as {user}')
            print(user)
            return redirect('contact:index',)
        messages.error(request,'Login failed')
    
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login',)
        
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    
    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been updated successfully')
            return redirect('contact:index',)
    is_update = True
  
    context = {
        'form': form,
        'is_update': is_update,
        'username': request.user,
               }
        
    return render(
        request, 'contact/register.html',
        context
        )
   
    
    