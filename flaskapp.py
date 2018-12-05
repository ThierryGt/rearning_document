# -*- coding: utf-8 -*- 
from flask.views import MethodView
from flask import Flask, render_template, request, redirect, url_for,session, Response 
from static.The_article.article import obtain_title
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from views.users.views import users_blueprint 
from views.chatbot.chatbot_views import chatbot_blueprint 
from views.wechat_exe.wechat_views import wechat_spider_blueprint 
from views.bank_data.bank_data_views import bank_data_blueprint
from views.my_index.index_views import index_blueprint
from views.Flask_TheForm.flask_form import form_blueprint
import pymysql
import time
import logging
import os
from wtforms import StringField
from wtforms.validators import InputRequired,ValidationError
from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextField
from wtforms.validators import DataRequired,Required
from wxpy import *
from functools import wraps
import sys
# print('\n'.join([''.join([('Thierry·Gt'[(x-y)%10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
# app = Flask(__name__, template_folder="templates", static_url_path="/xxxx")
app = Flask(__name__)
logging.basicConfig(filename='/var/www/flask/error.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
app.config['SECRET_KEY'] = 'any string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:passwd@addre:port/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config["CSRF_ENABLED"] = True
app.secret_key = "123456"
app.register_blueprint(users_blueprint)
app.register_blueprint(chatbot_blueprint)
app.register_blueprint(wechat_spider_blueprint)
app.register_blueprint(bank_data_blueprint)
app.register_blueprint(index_blueprint)
app.register_blueprint(form_blueprint)

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
APP_STATIC_TXT=os.path.join(APP_ROOT, "static/article")


@app.context_processor
def get_context_processor():
    data = os.listdir(os.path.join(APP_STATIC_TXT))
    # return dict(d = [d.split(".")[0] for d in data])
    return dict(d=data)


if __name__ == "__main__":
    app.run()
    # mongodb_conn() 


# flask 过滤器

# 字符串操作
{# 当变量未定义时,显示默认字符串,可以缩写为d #}
<p>{{name | default("No name", true)}}</p>

{# 单词首字母大写 #}
<p>{{ "hello" | capitalize }}</p>

{# 单词全小写 #}
<p>{{"XML" | lower}}</p>

{ # 去除字符串前后的空白字符 #}
<p>{{ " hello " | trim}}</p>

{ # 字符串反转, 返回"olleh" #}
<p>{{"hello" | reverse}}</p>

{ # 格式化输出,返回“Number is 2” #}
<p>{{ "%s is %d" | format("Number", 2)}}</p>

{ # 关闭HTML自动转义 #}
<p>{{"<em>name</em>" | safe}}</p>

{% autoescape false%}
{ # HTML转义, 即使autoescape关了也转义,可以缩写为e#}
<p>{{"<em>name</em>"}}</p>
{% endautoescape%}


# 数值操作
{ # 四舍五入取整, 返回13.0 #}
<p>{{ 12.8888 | round}}</p>

{ #向下截取到小数点后2位 #}
<{{ 12.8888 | round(2, "floor")}}>

{ #绝对值,返回12 #}
<p>{{-12 | abs}}</p>


# 列表操作
{# 取第一个元素}
<p>{{ [1,2,3,4,5] | first}}</p>

{# 取最后一个元素}
<p>{{ [1,2,3,4,5] | last}}</p>

{# 返回列表长度, 可以写为count#}
<p>{{ [1,2,3,4,5] | length}}</p>

{# 列表求和 }
<p>{{ [1,2,3,4,5] | sum}}</p>

{# 列表排序,默认为升序#}
<p>{{ [3,2,1,5,4] | sort}}</p>

{# 合并为字符串,返回"1|2|3|4|5"#}
<p>{{ [1,2,3,4,5] | join("|")}}</p>

{# 列表中所有元素都大写,这里可以用upper, lower， 但capitalize无效#}
<p>{{ ["tom", "bob", "ada" | upper]}}</p>


# 字典列表操作
{% set users=[{'name':'Tom','gender':'M','age':20},
              {'name':'John','gender':'M','age':18},
              {'name':'Mary','gender':'F','age':24},
              {'name':'Bob','gender':'M','age':31},
              {'name':'Lisa','gender':'F','age':19}]
%}

{# 按指定字段排序,这里设reverse为true使其按降序排#}
<ul>
{% for user in users | sort(attribute='age', reverse=true) %}
     <li>{{ user.name }}, {{ user.age }}</li>
{% endfor %}
</ul>

{# 列表分组，每组是一个子列表，组名就是分组项的值 #}
<ul>
{% for group in users|groupby('gender') %}
    <li>{{ group.grouper }}<ul>
    {% for user in group.list %}
        <li>{{ user.name }}</li>
    {% endfor %}</ul></li>
{% endfor %}
</ul>


{# 取字典中的某一项组成列表，再将其连接起来 #}
<p>{{ users | map(attribute='name') | join(', ') }}</p>


# Flask内置过滤器"tojson",变量输出为JSON字符串,可结合Javascript使用
# safe避免HTML自动转义
<script type="text/javascript">
var = users = {{users | tojson | safe}};
console.log(user[0].name);
</script>


# 自定义过滤器
def double_step_filter(l):
    return l[::2]
app.add_template_filter(double_step_filter, "double_step")
函数的第一个参数是过滤器函数,第二个参数是过滤器名称,
{ # 返回[1,3,5]}
<p>{{ [1,2,3,4,5] | double_step}}</p>

# 过滤器装饰器"template_filter"
@app.template_filter("sub")
def sub(l, start, end):
    return l[start:end]
# 返回[2,3,4]
<p>{{ [1,2,3,4,5] | sub(1,4)}}</p>


# 信号接收器,flask扩展可用到
from blinker import Namespace

app = Flask(__name__)
my_signals = Namespace()
model_saved = my_signals.signal('model_saved')


@app.route("/")
def index():
    model_saved.send(app, data1="A Signal", data2={1: 1})
    return "发送成功"


@model_saved.connect_via(app)           #装饰器，接收app通过model_saved发送而来的信号
def signal_recv(app,data1,data2):       #第一个参数app代表发送者，后面的参数为接收到的数据的键所对应的值
    print('信号接收函数:{0}，{1}'.format(data1,data2))
    pass


def gen_rnd_filename():
    filename_prefix = datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

# 控制文件上传大小(16M)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# 上传文件
@app.route("/upload",methods=['GET','POST'])
def upload():
    if request.method=="POST":
        fileobj = request.files["file"]
        fname, fext = os.path.splitext(fileobj.filename)
        upload_name = [".jpeg", ".jpg", ".gif", ".png"]
        if upload_name.count(fext) == 1:
            rnd_name = "%s%s"%(gen_rnd_filename(), fext)
            filepath = os.path.join(current_app.root_path, "static/uploads/%s"%rnd_name[0:8], rnd_name)
            dirname = os.path.dirname(filepath)
            if not os.path.exists(dirname):
                try:
                    os.makedirs(dirname)
                except:
                    return "创建目录失败"
            if not os.access(dirname, os.W_OK):
                return "创建目录不可写"
            fileobj.save(filepath)
            url = url_for("static", filename="%s/%s/%s"%("uploads", rnd_name[0:8], rnd_name))
            return url
        return "文件名不允许"
    return render_template('upload.html')


# 下载文件
@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('filepath', filename)):
            return send_from_directory('filepath', filename, as_attachment=True)
