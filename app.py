from flask import Flask, render_template, request

app = Flask(__name__)

ENV = "dev"

if ENV == "dev":
    app.debug = True
else:
    app.debug = False

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()