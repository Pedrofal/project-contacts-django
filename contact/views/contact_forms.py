from django.shortcuts import render, get_object_or_404, redirect  
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact
from django.contrib import messages






def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contact has been registered successfully')
            return redirect('contact:index')
        return render(
            request,
            'contact/create.html',
            context,
        )
    
    context = {
            'form': ContactForm(),
            'form_action': form_action,
            
            }
    return render(
            request,
            'contact/create.html',
            context,
            )
def update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'User has been updated successfully')
            return redirect('contact:index',)
    else:
        form = ContactForm(instance=contact)


    is_update = True
    
    context = {
        'form': form,
        'form_action': form_action,
        'is_update': is_update, 
    }
    
    return render(request, 'contact/create.html', context)

def delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True)
    contact.delete()
    messages.error(request, 'User has been deleted successfully')
    return redirect('contact:index')
