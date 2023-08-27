from django.apps import AppConfig


class AstroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'astro'
    def ready(self):
        import astro.signals