import os
import django
from django.utils import timezone
from faker import Faker
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from webblog.models import Blog  # Asegúrate de ajustar la ruta de importación según la ubicación de tu modelo Blog

fake = Faker()


def add_blog(n):
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        pub_date = timezone.now()  # O usa fake.date_time_between para fechas pasadas
        body = fake.text(max_nb_chars=2000)
        img_file = 'imagen.jpg'
        with open(img_file, 'rb') as file:
            Blog.objects.create(
                title=title,
                pub_date=pub_date,
                image=File(file, name=f"blog_{title.replace(' ', '_')}.jpg"),
                body=body
            )

if __name__ == '__main__':

    add_blog(10)  # Genera 10 entradas de blog
    # Llama aquí a las funciones para CreditRepair y ConsumerLaw si es necesario
