from flask import Flask, render_template, request, jsonify
from detector import FoodDetector

app = Flask(__name__)
detector = FoodDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    food_description = data.get('food', '')
    
    if not food_description:
        return jsonify({'error': 'Please provide food description'}), 400
    
    result = detector.analyze_food(food_description)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
