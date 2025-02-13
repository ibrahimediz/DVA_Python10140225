from app import app

@app.route("/")
def home():
    return "<h1>SELAMLAR____</h1>"