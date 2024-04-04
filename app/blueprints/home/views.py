from secrets import randbelow

from flask import Blueprint, render_template

home_bp = Blueprint(
    "home_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/home",
)


@home_bp.route("/")
def home() -> str:
    return render_template("home/index.html")


@home_bp.route("/random-number")
def random_number() -> str:
    return f"{randbelow(1000)}"
