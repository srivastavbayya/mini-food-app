import os
import logging
from flask import Flask, render_template, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

menu_items = [
    {"name": "Chicken Biryani", "price": 180},
    {"name": "Paneer Butter Masala", "price": 160},
    {"name": "Veg Fried Rice", "price": 120},
    {"name": "Masala Dosa", "price": 80},
]

@app.before_request
def log_request():
    print(f"Request received: {request.method} {request.path}", flush=True)

@app.route("/")
def home():
    return render_template("index.html", items=menu_items)

@app.route("/health")
def health():
    return {
        "status": "ok",
        "message": "Mini Food App is running"
    }

@app.route("/version")
def version():
    return {
        "app": "mini-food-app",
        "version": "1.0.0",
        "environment": os.environ.get("ENVIRONMENT", "development")
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
