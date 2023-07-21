from django.shortcuts import render
from .models import Client
from .forms import ClientForm


def clients(request):
    form = ClientForm(request.POST or None)
    clients = Client.objects.all()
    success = False
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        try:
            Client.objects.create(name=name, phone=phone)
            success = True
        except:
            pass
    return render(request, 'client.html', {"form": form,
                                           "clients": clients,
                                           "success": success})
# Create your views here.
