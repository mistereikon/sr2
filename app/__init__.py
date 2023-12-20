from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from app.resources import bp as api_bp
from app.html_views import html_bp

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"
api = Api(app)
jwt = JWTManager(app)

app.register_blueprint(api_bp)
app.register_blueprint(html_bp)

if __name__ == "__main__":
    app.run(debug=True)
