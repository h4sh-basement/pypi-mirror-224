from flask import Flask

app = Flask(__name__)


@app.route("/admin")
def admin():
    return "test"


def run():
    return app
