
from flask import Flask, request, redirect
import json

app = Flask(__name__)

CONFIG_FILE = "web_config.json"

def load():
    try:
        with open(CONFIG_FILE) as f:
            return json.load(f)
    except:
        return {"prefix": "!"}

def save(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    data = load()
    if request.method == "POST":
        data["prefix"] = request.form["prefix"]
        save(data)
        return redirect("/")
    return (
        "<h2>Vrindavan Bot Dashboard</h2>"
        "<form method='post'>"
        "Prefix: <input name='prefix' value='" + data['prefix'] + "'/>"
        "<button>Save</button>"
        "</form>"
    )

def run_dashboard():
    app.run(host="0.0.0.0", port=8080)
