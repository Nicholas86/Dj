from django.apps import AppConfig


class BlogsConfig(AppConfig):
    name = 'blogs'
    def ready(self):
        #connections.configure(**settings.ES_CONNECTIONS)
        import blogs.signals