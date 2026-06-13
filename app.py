from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/trade", methods=["POST"])
def trade():
    data = request.json
    
    symbol = data.get("symbol")
    action = data.get("action")
    lot = data.get("lot")

    print(f"Trade request: {action} {symbol} Lot: {lot}")

    return jsonify({
        "status": "success",
        "message": f"{action} order received for {symbol}"
    })

app.run(host="0.0.0.0", port=3000)
