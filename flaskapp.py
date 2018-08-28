from flask import Flask, render_template, request, redirect, session
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
# from log import logger
# from config import MYSQL_CONNE
from pymongo import MongoClient as mc
import logging
import os
# import functools
import sys
from wxpy import *
# app = Flask(__name__, template_folder="templates", static_url_path="/xxxx")
app = Flask(__name__)
logging.basicConfig(filename='/var/www/flask/error.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def mongodb_conn():
    conn = mc('127.0.0.1', 27017)
    # 连接mydb数据库，没有则自动创建
    db = conn.mydb
    #使用test_set集合，没有则自动创建 
    my_set = db.test
    for i in my_set.find():
        print(i)

def log():
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("error.log")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    logger.addHandler(handler)
    logger.addHandler(console)

weixinchatbot = ChatBot("weixinchatbot", storage_adapter='chatterbot.storage.MongoDatabaseAdapter',database='chatterbot', read_only=True)
# weixinchatbot = ChatBot("weixinchatbot", storage_adapter='chatterbot.storage.SQLStorageAdapter',database='chatterbot', read_only=True)
weixinchatbot.set_trainer(ChatterBotCorpusTrainer)
weixinchatbot.train("chatterbot.corpus.chinese")
"""
@app.route("/login", methods=["GET", "POST"])
@wapper
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        if user == "zxc" and pwd == "123":
            session["user_info"] = user
            return redirect("/index")
        else:
            return render_tmpalate("login.html", **{"msg": "username or password error"})
"""
@app.route('/', )
def hello_world():
    # return render_template("index.html")
    # return "Hello World"
    # return render_template("work_index.html")
    userText = request.args.get("key")
    if userText is not None:
        app.logger.info("my first logging")
        return str(weixinchatbot.get_response(userText))
        # return userText
    else:    
        return render_template("index.html")

"""
@app.route("/get")
def get_bot_response():
    userText = request.args.get("user_msg")
    passwdText = request.args.get("pass_wd")
    return "Hello"
"""


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # userText = request.args.get("key")
    # logging.basicConfig(filename="/var/www/flask/error.log",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if userText is not None:
        conn = mc("127.0.0.1", 27017)
        db = conn.mydb
        r_data = db.test
        r_data.insert({"d": userText})
        
        return str(weixinchatbot.get_response(userText))
    else:
        return "what?"

@app.route("/login")
def user_login():
    return render_template("user_login.html") 

@app.route("/loginsuccess")
def login_success():
    return "what are you doing?"

@app.route("/test_post", methods=['POST'])
def test_port():
    return request.get_data() 

def connectdb(user_input):
	db = pymysql.connect(
		host = MYSQL_CONNE['HOST'], 
		port = MYSQL_CONNE['PORT'],
		user=MYSQL_CONNE['USER'],
		passwd=MYSQL_CONNE['PASSWD'],
		db=MYSQL_CONNE['DB'],
		charset = "utf8",
		cursorclass = pymysql.cursors.DictCursor ,
		)
	cursor = db.cursor()
	try:
		# CREATE DATABASE DATA CHARACTER SET UTF8;
		# create table d(id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255));
		cursor.execute("INSERT INTO text(t) VALUES(%s)", [user_input])
		db.commit()
	except Exception as  e:
		db.rollback()
		print(e)
	finally:
		cursor.close()
		db.close()

if __name__ == "__main__":
    app.run()
    # mongodb_conn()

