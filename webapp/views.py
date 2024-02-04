from django.shortcuts import render, get_object_or_404
from webblog.models import Blog
from .models import AboutUs, Services, CreditRepair, ConsumerLaw
def home(request):
    # Obtener los últimos 2 posts de blog
    latest_blogs = Blog.objects.order_by('-pub_date')[:2]
    
    # Obtener los primeros 3 servicios
    featured_services = Services.objects.all()[:3]
    
    # Pasar los blogs y servicios al contexto de la plantilla
    context = {
        'latest_blogs': latest_blogs,
        'featured_services': featured_services,  # Añade los servicios al contexto
    }
    return render(request, 'webapp/home.html', context)

def aboutus(request):
    aboutus = AboutUs.objects.all()
    return render(request, 'webapp/aboutus.html', {'aboutus': aboutus})

def services(request):
    services = Services.objects.all()
    return render(request, 'webapp/services.html', {'services': services})

def service(request, id):
    # Busca el servicio específico por ID y si no se encuentra, devuelve un error 404
    service = get_object_or_404(Services, id=id)
    return render(request, 'webapp/service.html', {'service': service})

def service(request, id):
    # Usa 'get_object_or_404' para manejar adecuadamente los casos de objetos no encontrados.
    service = get_object_or_404(Services, id=id)
    return render(request, 'webapp/service.html', {'service': service})

def creditrepair(request):
    creditrepair = CreditRepair.objects.all()
    return render(request, 'webapp/creditrepair.html', {'creditrepair': creditrepair})

def consumerlaw(request):
    consumerlaw = ConsumerLaw.objects.all()
    return render(request, 'webapp/consumerlaw.html', {'consumerlaw': consumerlaw})

def contact(request):
    return render(request, 'webapp/contact.html')