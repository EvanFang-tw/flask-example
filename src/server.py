from flask import Flask, jsonify, redirect, render_template, abort, request, url_for

app = Flask(__name__)

# Example: return string
@app.route("/")
def index():
    return "<h1>Flask is cool</h1>"


# Example: use template
@app.route("/hello")
def hello():
    return render_template("hello.html", message="world")


# Example: post form and redirect
@app.route("/form", methods=["GET", "POST"])
def get_form():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("greeting", username=username))
    else:
        return render_template("form.html")


@app.route("/sayhi/<username>")
def greeting(username):
    return f"<h1>Hi {username}</h1>"


# Example: return 404
@app.route("/404")
def not_found():
    abort(404)
    # or use return with message:
    # return "Oops! Not Found.", 404


# Example: return json list
@app.route("/api/list")
def get_list():
    data = [
        {
            "name": "David",
            "age": 18,
        },
        {
            "name": "Mary",
            "age": 61,
        },
    ]
    return jsonify(data)


# Example: get json into dict from request
@app.route("/api/data", methods=["POST"])
def create_data():
    app.logger.info(request.json)
    return "ok", 201
