#文档地址:https://elasticsearch-dsl.readthedocs.io/en/latest/

from django.conf import settings
from elasticsearch_dsl import DocType, Date, Keyword, Text, Index, MetaField, Nested, field, InnerDoc

from elasticsearch_dsl.connections import connections

"""
初始化连接。
alias:标签,字符串
hosts:服务器名称,数组。
hosts:elasticsearch.yml文件必须配置192.168.40.15, 默认的127.0.0.1无法访问。
原因:https://discuss.elastic.co/t/upgrade-elasticsearch-2-0-to-5-2-indexing-not-working/80241
"""
connection = connections.create_connection(hosts=["192.168.40.10", "192.168.99.1"])
#'http://192.168.0.232:9200/'
