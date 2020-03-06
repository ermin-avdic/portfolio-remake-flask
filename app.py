from flask import Flask, render_template, request

app = Flask(__name__)

ENV = "dev"

if ENV == "dev":
    app.debug = True
else:
    app.debug = False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        naslov = request.form["naslov"]
        poruka = request.form["poruka"]
    return render_template("index.html")

if __name__ == "__main__":
    app.run()