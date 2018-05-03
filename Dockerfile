
############################# 官网提供的 #######################
#FROM python:3
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
#WORKDIR /code
#ADD requirements.txt /code/
#RUN pip3 install -r requirements.txt
#ADD . /code/



############################# JTSERVER 项目里的 #######################
FROM nicholas86/dj_web_1:2

# FROM registry.cn-beijing.aliyuncs.com/io84/ubuntu_16_04
# MAINTAINER kevin@sinalifo.com

# 更换apt-get镜像
#RUN rm -f /etc/apt/sources.list
#ADD ./develop/aliyun-sources.list  /etc/apt/sources.list
#RUN apt-get clean
#RUN apt-get update -y
#RUN apt-get upgrade -y

#ENV LANG en_US.UTF-8
#ENV LANGUAGE en_US:en
#ENV LC_ALL en_US.UTF-8

#ENV C_FORCE_ROOT 1
#ENV PYTHONPATH ./:$PYTHONPATH
#ENV PYTHONUNBUFFERED 1
#
#RUN apt-get install -y --force-yes --fix-missing \
#	  vim \
#     git \
#     python \
#     python3-pip \
#     curl \
#     nginx \
#     libmysqlclient-dev \
#     # locales \
#     python-celery-common

#RUN locale-gen en_US.UTF-8

#RUN mkdir /workspace

ADD requirements.txt /workspace/
RUN pip3 install -r /workspace/requirements.txt
ADD . /workspace/
#RUN mkdir /uwsgi_conf
RUN /bin/sh -c /bin/sh -c mkdir /uwsgi_conf
COPY ./develop/uwsgi_params  /uwsgi_conf/uwsgi_params

WORKDIR /workspace

# ENTRYPOINT ["/usr/bin/supervisord"]
# CMD ["-c", "/etc/supervisor/supervisord.conf"]

EXPOSE 80
