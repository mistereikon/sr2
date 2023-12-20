from flask import Blueprint, render_template

html_bp = Blueprint("html", __name__)

@html_bp.route("/")
def index():
    return render_template("create_vacancy.html")
