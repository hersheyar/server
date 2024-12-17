from flask import Flask, jsonify


app = Flask(__name__)

@app.get("/")

def home():
    return "Hello from Flask"

@app.get("/string")
def string():
    hi = {"message":"Hello as a string var"}
    return jsonify(hi)


app.run(debug=True)

