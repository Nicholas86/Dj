#!/bin/bash
echo "开始执行utils脚本"

#1.自定义waituntil函数
waituntil (){
    #声明局部变量
    local count=0
    local limit="${1}"
    local msg="${2}"
    #shift命令用于对参数的移动(左移) 2位
    shift 2

    echo "进入 waituntil函数"

    #while循环的条件测试是测真值，until循环则是测假值。
    until echo "trying to ${msg} $((count+1))" && "$@"
    do
        count=$((count+1))
        sleep 5
        echo "睡眠5s"

        if [ "$count" -ge "$limit" ]
        then
            echo "failed to ${msg}"
            exit 1
        fi
    done
}

#2.自定义ensure函数, reset脚本调用
ensure () {
  local msg="$1"
  shift
  echo "ensure函数:${msg}"
  "$@" || exit 1
}

# $@:传给脚本的所有参数的列表