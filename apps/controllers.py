# -*- encoding:utf-8 -*-

from flask import Flask, redirect, url_for, render_template,request, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from apps import app, db
from models import Article, Comment, User
from form import JoinForm, LoginForm
from sqlalchemy import desc
import pusher


@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

@app.route('/test')
def test():
    return render_template('list.html')