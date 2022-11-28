from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Enter the area name!"

@app.route("/<area_name>")
def show(area_name=None):
    return render_template("area_code.html",area_name=area_name)

if "__name__" == "__main__":
    app.run()
