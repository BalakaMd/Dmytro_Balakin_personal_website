from flask import Flask, abort, render_template, redirect, url_for, flash, request, send_file
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
import os

# Import your forms from the forms.py

# APP Initialization
app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/download')
def download_cv():
    return send_file(path_or_file='static/Resume.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
