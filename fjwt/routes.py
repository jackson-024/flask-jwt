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

        if "x-access-token" in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({"message" : "Token missing"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"],algorithms="HS256")
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

    email = data['email']
    password = data['password']

    user = Users.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        token = jwt.encode({
            'email' : user.email,
            'exp' :datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        },
        
         app.config["SECRET_KEY"],
         "HS256")

        return token
    
    return ""

@app.route("/about", methods=['GET'])
@token_required
def about(current_user):
    return jsonify({
        "Message": "Authenticated"
    })