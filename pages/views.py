from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm
# Create your views here.

def home_view(request):
    return render(request, 'home.html', {})

def about_view(request):
    return render(request, 'about.html', {})

def stripe_view(request):
    return render(request, 'stripe.html', {})

def contact_view(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        
        html = render_to_string('email.html', form_data)
        # message = '''
        # From:\n\t\t{}\n
        # Message:\n\t\t{}\n
        # Email:\n\t\t{}\n
        # Phone:\n\t\t{}\n
        # '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
        
        subject = "TaeKwonDo Of Morganville Website Contact Form: " + name
        send_mail(subject, message, '', ['aravindg.usa@gmail.com', 'taekwondoofmorganville@aol.com'], fail_silently=False, html_message=html) # TODO: enter your email address
        
    return render(request, 'contact.html', {})   