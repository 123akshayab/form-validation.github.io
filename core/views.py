from django.views.generic import View, ListView
from django.shortcuts import render, redirect

from core.forms import ContactForm
from core.models import Contact

class ContactView(View):
    
    def get(self, request):
        form = ContactForm() 
        return render(request, "core/contact.html", {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST, request.FILES) 
        if form.is_valid():
            instance = form.save()
            return render(request, "core/success.html", {"data": instance})
        else:
            return render(request, "core/contact.html", {"form": form})

class ContactListView(ListView):
    template_name = "core/contact-list.html"
    context_object_name = "records"
    queryset = Contact.objects.all()

class ContactUpdateView(View):

    def get(self, request, id):
        form = ContactForm(instance=Contact.objects.get(id=id))
        return render(request, "core/contact.html", {"form": form})
    
    def post(self, request, id):
        form = ContactForm(request.POST, request.FILES, instance=Contact.objects.get(id=id))
        if form.is_valid():
            instance = form.save()
            return redirect("list-contact")
        else:
            return render(request, "core/contact.html", {"form": form})
