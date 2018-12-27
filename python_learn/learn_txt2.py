print({
    "telnet": "可连接目标服务器和端口并输入命令",
    "http处理所有客户端-服务器HTTP请求": {
        "client": "处理客户端请求",
        "server": "协助编写PythonWeb服务器程序",
        "cookies和cookiejar": "会处理cookie, cookie可以在请求中存储数据",
    },
    "urllib基于http的高层库": {
        "request": "处理客户端请求",
        "response": "处理服务端的响应",
        "parse": "会解析URL",
    },
    "response.status": {
        "1xx(信息)": "服务器收到了请求,但是需要客户端发送一些额外的信息",
        "2xx(成功)": "请求成功, 出了200意外, 其他的状态码还会包含一些特殊含义",
        "3xx(重定向)": "资源位置发生改变, 所以响应会返回一个新的URL给客户端",
        "4xx(客户端错误)": "客户端发送错误, 404(页面不存在)",
        "5xx(服务端错误)": "502(网关错误)",
    },
    "python -m http.server": "可用于个别文件传输",
    "apache": {
        "apache守护模式": "会产生一个或多个独立于apache的进程"
    },
    "file": {
        "open()": "创建文件",
        "exists()": "检查文件是否存在",
        "isfile()": "检查是否为文件, 检查名称是文件, 目录, 还是符号链接",
        ".": "表示当前目录",
        "..": "表示上层目录",
        "isabs()": "判断参数是否是一个绝对路径名, 参数不需要是一个真正的文件",
        "copy()": "文件复制",
        "rename()": "重命名文件",
        "link()": "创建一个硬链接",
        "symlink()": "创建一个符号链接",
        "islink()": "检查参数是文件还是符号链接",
        "chmod()": "修改权限",
        "chown()": "修改所有者",
        "abspath()": "获取路径名",
        "realpath()": "获取符号链接的路径名",
        "remove()": "删除文件",
    },
    "directory": {
        "mkdir()": "创建目录",
        "rmdir()": "删除目录",
        "listdir()": "列出目录内容, 返回列表的形式",
        "chdir()": "修改当前目录",
        "glob()/列出匹配文件": {
            "*": "匹配任意名称(re中是.*)",
            "?": "会匹配一个字符",
            "[abc]": "会匹配字符a,b,c",
            "[!abc]": "会匹配除了a,b,c之外的所有字符",
        },
    },
    "subprocess创建进程": {
        "getoutput()": "获取Unix date程序的输出, 可添加参数,管道,I/O重定向<和>",
        "check_output()": "接受一个命令和参数列表, 默认情况下返回的不是字符串\
                               而是字节类型的标准输出, 这个函数并没有shell",
        "getstatusoutput()": "获取程序的退出状态, 返回一个包含状态码和输出的元组",
        "call()": "退出状态, 状态0通常表示运行成功",
        },
    "multiprocessing创建进程": "支持任务队列和进程间通信",
    "日期与时间": {
        "calendar.isleap()": "检测是否是润年",
        "datetime": {
            "isoformat()": "输出datetime对象, 中间的T会把日期和时间分割开",
            "now()": "获取当前日期和时间",
            "combine()": "把一个date对象和一个time对象合并成一个datetime对象",
        },
        "date": {
            "isoformat()": "输出date对象",
            "today()": "生成当天的日期",
            "timedelta()": "可实现对date的加法",
            "date.min": "范围(年=1, 月=1, 日=1)",
            "date.max": "范围(年=9999, 月=12，日=31)",
            "time": "表示一天中的时间",
            "datetime()": "直接创建一个年月日时分秒微秒的参数",
        },
        "time": {
            "time.time()": "返回当前时间的纪元值",
            "ctime()": "把纪元值转换成字符串",
            "localtime()": "会返回当前系统时区下的时间",
            "gmtime()": "会返回UTC时间",
            "localtime()": "返回当前系统时区下的时间, 返回struct_time对象",
            "gmtime()": "返回UTC时间, 返回struct_time对象",
            "mktime()": "把struct_time对象转换回纪元值",
        },
    },
})


def time():
    import time
    # 时间戳
    now = time.time()



def datetime():
    from datetime import datetime, time, date
    now = datetime.now()
    # now.montu 12     
    # now.day 27
    # now.hour 13
    # now.minute 27
    # now.second 34
    # now.microsecond
    noon = time(12)
    this_day = date.today()
    noon_today = datetime.combine(this_day, noon)
    # 获取noon_today中的年月日
    noon_today.date()
    # 获取noon_today中的时分
    noon_today.time()



def date():
    from datetime import time
    noon = time(12, 0, 0)
    # noon.hour 12
    # noon.second 0
    # noon.microsecond 0
    import calendar
    calendar.isleap()
    from datetime import date
    halloween = date(2014, 10, 31)
    # halloween.day 31
    # halloween.month   10
    # halloween.year    2014
    halloween.isoformat()
    # "2014-10-31", iso指ISO 8601, 一种表示日期和时间的国际标准
    from datetime import date
    date.today()
    from datetime import timedelta
    # 天数加1, 也可使用乘法,
    timedelta(days=1)
    


def subprocess():
    import subprocess
    subprocess.getoutput("date")
    # 'Thu Dec 27 02:20:50 UTC 2018' 
    subprocess.getoutput("date -u | wc")
    # '      1       6      29'
    ret = subprocess.check_output(["date", "-u"])
    # b'Thu Dec 27 02:21:24 UTC 2018\n'
    subprocess.call("date -u", shell=True)
    # 加上参数shell=True, 这样函数就会用shell来执行命令


def directory_glob():
    import glob
    # 获取所有以m开头的文件和目录
    glob.glob("m*")
    # 获取名称为8个字符且以m开头e结尾的文件和目录
    glob.glob("m??????e")
    # 获取所有以k, l或m开头且以e结尾的文件和目录
    glob.glob("[klm]*d")



def directory_chdir():
    import os
    # 跳转到directory_name目录
    os.chdir(directory_name)



def directory_listdir():
    import os
    # 返回列表的形式
    os.listdir(directory_name)


def directory_rmdir():
    import os
    os.rmdir(directory_name)


def directory_mkdir():
    import os
    os.mkdir(directory_name)


def file_remove():
    import os
    # 删除文件
    os.remove(file_name)


def file_realpath():
    import os
    # 返回符号链接路径名, 包含文件名
    os.path.realpath(file_name)


def file_abspath():
    import os
    # 获取当前文件路径名, 包含文件名
    os.path.abspath(file_name)


def file_link():
    import os
    # 硬链接
    os.link("oops.txt", "yikes.txt")
    # 符号链接
    os.symlink("oops.txt", "jeepers.txt")


def file_rename():
    import os
    # 重命名文件
    os.rename("ohno.txt", "ohwell.txt")


def file_copy():
    import shutil
    # oops.txt复制到文件ohno.txt
    shutil.copy("oops.txt", "ohno.txt")
    # 复制一个文件并删除原始文件
    shutil.move("oops.txt", "ohno.txt")


def file_isabs():
    import os
    os.path.isabs(path_name)
    

def file_isfile():
    import os
    # 判断是否是文件
    os.path.isfile(file_name)
    # 判断目录的方法
    os.path.isdir(directory_name)


def file_exists():
    import os
    os.path.exists("oops.txt")
    os.path.exists(".")


# apache守护模式, 配置文件添加内容
# WSGIDaemonProcess domain-name user=user-name group=group-name threads=25
# WSGIProcessGroup domain-name



