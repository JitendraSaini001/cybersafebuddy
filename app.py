from flask import Flask, request, jsonify
from advice_logic import generate_advice
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

@app.route("/api/advice", methods=["POST"])
def get_advice():
    data = request.json
    advice = generate_advice(data)
    return jsonify({"advice": advice})

if __name__ == "__main__":
    app.run(debug=True)
