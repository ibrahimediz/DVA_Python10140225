from app import app

ornek = [
    {"id": 1, "name": "ali"},
    {"id": 2, "name": "veli"},
    {"id": 3, "name": "ahmet"},
]

@app.route("/")
def home():
    return "<h1>SELAMLAR____</h1>"

@app.route("/ornek")