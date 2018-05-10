#文档地址:https://elasticsearch-dsl.readthedocs.io/en/latest/

from django.conf import settings
from elasticsearch_dsl import DocType, Date, Keyword, Text, Index, MetaField, Nested, field, InnerDoc

from elasticsearch_dsl.connections import connections

"""
初始化连接。
alias:标签,字符串
hosts:服务器名称,数组
"""
connection = connections.create_connection(hosts=['http://127.0.0.1:9200/'])