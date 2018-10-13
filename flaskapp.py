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
