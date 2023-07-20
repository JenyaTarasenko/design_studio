from django.shortcuts import render
from django.views.generic import CreateView
from django.views import View

from .forms import ContactForm
from .models import ContactLink


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {'contacts': contacts, 'form': form})



class CreateContact(CreateView):#после заполнеия формы переход на главную
    form_class = ContactForm
    success_url ='/'