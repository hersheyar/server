from flask import Flask, jsonify, request, render_template
import json
app = Flask(__name__)

@app.get("/")
def home():
    return "Welcome to the flask API"


@app.get("/about")
def about_page():
    return render_template("about.html") # rebder_template is reserved and look for a template folder


hi = {"message":"Hello as a string var"}
@app.get("/string")
def astringy():
    return jsonify(hi)


products = []

@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f"this is my new product {product}")
    products.append(product)
    return jsonify(products)

@app.get("/api/products")
def get_product():
    return jsonify(products)


@app.get("/api/products/count")
def get_product_count():
    product_count = len(products)
    return {"Number Of Products": product_count}



@app.put("/api/products/<int:index>")
def update_priduct(index):
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

app.run(debug=True)




