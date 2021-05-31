from flask import Flask, render_template, request
from flask.globals import request
from Lesson_19_flask.views import products_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")

@app.route("/", methods=["GET", "POST"])
def index():
    name = "World"
    if request.method == "POST":
        name = request.form.get("name", "World")
    return render_template("index.html", name=name)
 
    #     return f"<h1> Hello {request.form.get('name', 'World')}! </h1>"
    # return "<h1> Hello World! </h1>"

@app.route("/hello/")
@app.route("/hello/<string:name>/")
def hello(name = None):
    if name is None:
        name = "World"
    return f"<h1> Hello {name} ! </h1>"

@app.route("/post/<int:post_id>/")
def show_post(post_id):
    return "Post int %r" %post_id