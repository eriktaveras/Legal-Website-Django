from django.shortcuts import render
from .models import AboutUs, Services, CreditRepair, ConsumerLaw

# Create your views here.


def index(request):
    return render(request, "webapp/index.html")

def aboutus(request):
    aboutus = AboutUs.objects.all
    return render(request, 'webapp/aboutus.html', {'aboutus' : aboutus})

def services(request):
    services = Services.objects.all()
    return render(request, 'webapp/services.html', {'services' : services})

def service(request, id):
    service = Services.objects.get(id=id)
    return render(request, 'webapp/service.html', {'service' : service})

def home(request):
    return render(request, 'webapp/home.html', {'home' : home})

def creditrepair(request):
    creditrepair = CreditRepair.objects.all
    return render(request, 'webapp/creditrepair.html', {'creditrepair' : creditrepair})

def consumerlaw(request):
    consumerlaw = ConsumerLaw.objects.all
    return render(request, 'webapp/consumerlaw.html', {'consumerlaw' : consumerlaw})

