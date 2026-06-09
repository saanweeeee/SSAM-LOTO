# from flask import Flask
# from flask import request
# from flask import jsonify

# from flask_cors import CORS

# from predictor import predict_equipment
# from loto_data import LOTO_DATA

# import os

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = "uploads"

# os.makedirs(
#     UPLOAD_FOLDER,
#     exist_ok=True
# )

# @app.route("/predict", methods=["POST"])
# def predict():

#     if "image" not in request.files:
#         return jsonify({
#             "error": "No image uploaded"
#         }), 400

#     image = request.files["image"]

#     path = os.path.join(
#         UPLOAD_FOLDER,
#         image.filename
#     )

#     image.save(path)

#     equipment, confidence = predict_equipment(path)

#     return jsonify({
#         "equipment": equipment,
#         "confidence": round(confidence, 2),
#         "checklist": LOTO_DATA[equipment]
#     })

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import traceback

print("Starting app...")

try:
    from predictor import predict_equipment
    print("✓ Predictor imported")
except Exception:
    print("✗ Failed to import predictor")
    traceback.print_exc()
    raise

try:
    from loto_data import LOTO_DATA
    print("✓ LOTO data imported")
except Exception:
    print("✗ Failed to import loto_data")
    traceback.print_exc()
    raise

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

print("✓ Flask initialized")


@app.route("/")
def home():
    return jsonify({
        "message": "LOTO API Running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(path)

    equipment, confidence = predict_equipment(path)

    return jsonify({
        "equipment": equipment,
        "confidence": round(confidence, 2),
        "checklist": LOTO_DATA[equipment]
    })


if __name__ == "__main__":
    print("✓ Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)