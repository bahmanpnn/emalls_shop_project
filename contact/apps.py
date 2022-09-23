from tabnanny import verbose
from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
    verbose_name='ماژول تماس با ما'