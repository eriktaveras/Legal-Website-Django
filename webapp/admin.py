from django.contrib import admin
from .models import AboutUs, Services, CreditRepair, ConsumerLaw

# Register your models here.

admin.site.register(AboutUs, )
admin.site.register(Services, )
admin.site.register(CreditRepair, )
admin.site.register(ConsumerLaw, )

