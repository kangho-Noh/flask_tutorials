from flask import Flask

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return "Hello! Welcome to mi casa!"


@app.route("/<username>")
def potato(username):
    return f"Hello your name is {username}"


app.run(host="127.0.0.1")
