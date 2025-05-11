from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})

@app.route("/geocoords")
def coords():
    try:
        address = request.args.get("q")
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": address,
            "format": "json",
            "limit": 1
        }

        response = requests.get(url, params=params, headers={"User-Agent": "GeoApp/1.0"})
        response.raise_for_status()
        data = response.json()

        if not data:
            return jsonify({"error": "Adress not found"}), 404
        
        result = {
            "lat": float(data[0]["lat"]),
            "lon": float(data[0]["lon"]),
            "display_name": data[0]["display_name"]
        }

        return jsonify(result)
    
    except requests.RequestException as err:
        return jsonify({"error": str(err)}), 500
    
@app.route("/georoute", methods=['POST'])
def route():
    req = request.get_json()
    start = req.get("start")
    end = req.get("end")
    if not start or not end:
        return jsonify({"error": "Start and end required"}), 400

    payload = {
        "coordinates": [start, end]
    }
    url = 'https://api.openrouteservice.org/v2/directions/driving-car'
    key = os.getenv('API_KEY')
    try:
        response = requests.post(
            url,
            json=payload,
            headers={"Authorization": key, "Content-Type": "application/json"}
        )
        response.raise_for_status()
        data = response.json()

        if not data:
            return jsonify({"error": "Adress not found"}), 404

        return jsonify(data)
    
    except requests.RequestException as err:
        return jsonify({"error": str(err)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
