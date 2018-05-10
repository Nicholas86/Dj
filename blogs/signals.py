from django.db.models.signals import post_save
from django.dispatch import receiver

from blogs.models import Blog
# Signal to save each new blog post instance into ElasticSearch

@receiver(post_save, sender=Blog, dispatch_uid="create_es_blog_index_doc")
def create_es_blog_index_doc(sender, instance, **kwargs):
    instance.create_es_blog_index_doc(**kwargs)