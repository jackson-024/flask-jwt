from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "fc90955c1ea67d182824cbb6d3c7d35c"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://escalation_sys:escalation_sys2021@localhost/escalation_sys"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from fjwt import routes