from django.contrib import admin
from django.urls import path, include
from webapp.views import aboutus, services, service, home, creditrepair, consumerlaw, contact
from django.conf.urls.static import static
from django.conf import settings
from webblog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('aboutus/', aboutus),
    path('services/', services),
    path('services/<int:id>/', service, name='service_detail'),
    path('creditrepair/', creditrepair),
    path('consumerlaw/', consumerlaw),
    path('blog/', views.allblogs , name='allblogs'),
    path('blog/<int:blog_id>/', views.detail, name="detail"),
    path('contact/', contact, name='contact'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


