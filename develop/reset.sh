#!/bin/bash

#1.获取脚本的绝对路径
absolute_path="$(cd $(dirname ${BASH_SOURCE[0]}) && pwd )"
echo "当前脚本的绝对路径: ${absolute_path}"

#2.引用外部脚本, 并pwd打印当前脚本的绝对路径
source "$(cd $(dirname ${BASH_SOURCE[0]}) && pwd)/utils.sh"

#3.kill强制停止服务容器
ensure "killing existing services" docker-compose kill

#4.rm删除所有(停止状态)容器
ensure "removing existing services" docker-compose rm -fv
ensure "removing existing services" docker-compose rm -fv

#4.1清空elasticsearch索引、文档
ensure "starting elasticsearch" brew services restart elasticsearch
sleep 10
ensure "removing existing elasticsearch index-doc" curl -XDELETE http://192.168.99.1:9200/_all

#5.判断是否包含BUILD参数, BUILD=Y ./develop/reset.sh 参数名BUILD, 值Y
if [ -n "${BUILD}" ]
then
    ########################
        #构建服务容器, 执行build命令时,
        #会执行docker-compose文件里的相关操作,
        #再执行Dockerfile文件里的相关操作,
        #最后执行下面的命令
    #####################
    ensure "building services" docker-compose build
fi

if [ -n "${PULL}" ]
then
    ensure "pulling images" docker-compose pull
fi

#6.后台唤醒服务容器
ensure "starting services" docker-compose up -d

#7.因为Django web服务依赖MySQL数据库服务, 所以需要等待20s, 直到MySQL服务启动。否则Django setting里面MySQL数据库配置出错
###### 移除web服务 ######
ensure "waiting db services to come up" docker-compose run --rm web sleep 20

#8.Django连接数据库后,迁移数据库
# ensure "creating tables" docker-compose run --rm web python3 manage.py makemigrations
ensure "migrate db tables" docker-compose run --rm web python3 manage.py migrate

#9.Django连接数据库后,再次重启web服务
# ensure "migrate activity db tables" docker-compose run --rm web python3 manage.py migrate --database=activity_stream
ensure "restart web" docker-compose restart web


if [ -z "${NOLOAD}" ]
then
    ensure "loading test data" docker-compose run --rm web python3 manage.py loaddata develop/djdb.json
    # ensure "uploading files" docker-compose run --rm web bash -c 'PYTHONPATH="."  python3 develop/upload.py'
fi
