from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app import app

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username == "your_username" and password == "your_password":
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}, 200
    else:
        return {"message": "Invalid credentials"}, 401
