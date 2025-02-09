from flask import Flask, jsonify, request
from flask_cors import CORS
from storage import activity_storage

app = Flask(__name__)
CORS(app)  # Включаем CORS

@app.route("/api/get_activity", methods=["GET"])
def get_activity():
    key = request.args.get("key")
    if not key:
        return jsonify({"error": "Ключ не указан"}), 400

    activity_data = activity_storage.get(key)
    if activity_data:
        return jsonify(activity_data)
    return jsonify({"error": "Данные не найдены"}), 404

if __name__ == "__main__":
    app.run(debug=True)
