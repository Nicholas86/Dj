from django.apps import AppConfig


class BlogsConfig(AppConfig):
    name = 'blogs'
    verbose_name = '    博客'
    def ready(self):
        #connections.configure(**settings.ES_CONNECTIONS)
        print("信号来啦🌶")
        import blogs.signals