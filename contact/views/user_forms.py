from django.shortcuts import render, redirect
from contact.forms import RegisterForm
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form = form.save()
                return redirect('contact:index',)
    return render(
        request, 'contact/register.html',
        {'form': form}
        )