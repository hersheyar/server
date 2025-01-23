from flask import Flask, jsonify, request, render_template
import json
from config import products_db, coupons_db

app = Flask(__name__)

@app.get("/")
def home():
    return "Welcome to the flask API"


@app.get("/about")
def about_page():
    return render_template("about.html") # render_template is reserved and look for a template folder


hi = {"message":"Hello as a string var"}
@app.get("/string")
def astringy():
    return jsonify(hi)



def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.post("/api/products")
def save_product():
    print("Post received")
    product = request.get_json()
    print(f"this is my new product {product}")
    products_db.products.insert_one(product)
    return json.dumps(fix_id(product))


@app.get("/api/products")
def get_product():
    products = []
    cursor = products_db.products.find()
    for prod in cursor:
        products.append(fix_id(prod))
    return jsonify(products)


@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product = request.get_json()
    print(f"Product: {updated_product}: {index}")


    if 0 <= index <= len(products):
        products[index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist"

@app.delete("/api/products/<int:index>")
def delete_product(index):
        print(f"delete: {index}")

        if index >=0 and index < len(products):
            deleted_product = products.pop(index)
            return json.dumps(deleted_product)
        else:
            return "That index does not exist"



##############



@app.post("/api/coupons")
def save_coupon():
    print("Post received")
    coupon = request.get_json()
    print(f"this is my new coupon {coupon}")
    coupons_db.coupons.insert_one(coupon)
    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    coupons = []
    cursor = coupons_db.coupons.find()
    for prod in cursor:
        coupons.append(fix_id(prod))
    return jsonify(coupons)

app.run(debug=True)




