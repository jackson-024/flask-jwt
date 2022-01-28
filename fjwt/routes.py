from flask import jsonify, request, jsonify, make_response
from flask_login import current_user
from fjwt import app, bcrypt
from fjwt.models import Users
import jwt
import datetime
from functools import wraps

#Verify token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({"message" : "Token missing"}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Users.query.filter_by(email=data['email']).first()

        except:
            return jsonify({
                "Message" : "Token is inavalid"
            }), 401

        return f(current_user, *args, **kwargs)
    return decorated

@app.route("/login", methods=["POST"])
def login():
    data =  request.get_json()

    email = data['username']
    password = data['password']

    user = Users.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        token = jwt.encode({
            'user_id' : user.user_id,
            'exp' :datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config["SECRET_KEY"])
        return token
    return ""

@app.route("/about")
@token_required
def about():
    return jsonify({
        "Message": "Authenticated"
    })