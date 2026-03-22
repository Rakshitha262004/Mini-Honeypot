from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

LOG_FILE = "logs/dashboard.json"

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/logs")
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"total": 0, "unique": 0, "high": 0, "countries": 0, "logs": []})

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    total = len(data)
    unique = len(set(i["ip"] for i in data))
    high = len([x for x in data if x["severity"] == "HIGH"])
    countries = len(set(i["country"] for i in data))

    return jsonify({
        "total": total,
        "unique": unique,
        "high": high,
        "countries": countries,
        "logs": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
