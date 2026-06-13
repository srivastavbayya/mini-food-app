from flask import Flask, render_template

app = Flask(__name__)

menu_items = [
    {"name": "Chicken Biryani", "price": 180},
    {"name": "Paneer Butter Masala", "price": 160},
    {"name": "Veg Fried Rice", "price": 120},
    {"name": "Masala Dosa", "price": 80},
]

@app.route("/")
def home():
    return render_template("index.html", items=menu_items)

@app.route("/health")
def health():
    return {"status": "ok", "message": "Mini Food App is running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    