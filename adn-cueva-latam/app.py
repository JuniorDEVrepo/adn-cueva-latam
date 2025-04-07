from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = "adn_completados.json"

@app.route("/")
def home():
    return render_template("adn_cueva.html")

@app.route("/guardar", methods=["POST"])
def guardar():
    data = {
        "discord_id": request.form.get("discord_id"),
        "clave": request.form.get("clave")
    }
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").write("[]")

    with open(DATA_FILE, "r") as f:
        datos = json.load(f)

    datos.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(datos, f, indent=4)

    return "✅ Gracias por enviar tu ADN. Pronto serás reconocido en la Cueva."

if __name__ == "__main__":
    app.run(debug=True)
