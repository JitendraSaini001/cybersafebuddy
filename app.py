from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve your HTML file

@app.route('/get-advice', methods=['POST'])
def get_advice():
    # Simulate personalized advice based on input
    data = request.json  # Get JSON data from frontend
    age = data.get('age')
    wifi_usage = data.get('wifi')
    
    # Example personalized advice
    advice = []
    
    if age == '50plus':
        advice.append("Consider using a VPN on public Wi-Fi.")
    if wifi_usage == 'yes':
        advice.append("Always avoid using public Wi-Fi for financial transactions.")
    
    # Return advice as a JSON response
    return jsonify({"advice": advice})

if __name__ == '__main__':
    app.run(debug=True)
