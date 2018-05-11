from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl import DocType, Text, Date, Integer, Boolean, Completion, Search, Nested, InnerDoc, connections, \
    Q

from blogs.es_client import connection

from django.conf import settings

class BlogIndexDoc(DocType):
    id = Integer()
    title = Text(analyzer='ik_max_word', search_analyzer="ik_max_word")
    content = Text(analyzer='ik_max_word', search_analyzer="ik_max_word")
    char_num = Integer()
    is_comments_enabled = Boolean()
    like_numbers = Integer()
    category = Text(analyzer='ik_max_word', search_analyzer="ik_max_word")
    tags = Text(analyzer='ik_max_word', search_analyzer="ik_max_word")
    create_date = Date()
    suggestions = Completion()

    class Meta:
        index = settings.ELASTICSEARCH_INDEX_NAME  #索引
        doc_type = "blog"