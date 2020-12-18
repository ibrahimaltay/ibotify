from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'X23dFpNP55v_qLOimyjlARv7CBdGwWXDKVbyqZYIlhLXKMmeCQoKQRNSCoVmWrgbxlVh8uaeOHqMtzTdF1U7Bg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from appmain import routes