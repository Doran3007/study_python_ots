from flask import Blueprint, render_template
from werkzeug.exceptions import BadRequest

products_app = Blueprint("products_app", __name__)

PRODUCTS = {
    1: "Smartphone",
    2: "Tablet",
    3: "Laptop",
}


@products_app.route("/")
def product_list():
    return render_template("products/index.html", products=PRODUCTS)

@products_app.route("/<int:product_id>/", endpoint="product_detail")
def product_detail(product_id:int):
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        raise BadRequest(f"invalid product id #{product_id}")
    
    return render_template("products/detail.html", product_id=product_id, product_name=product_name)
