from flask import Flask, render_template, request, jsonify
from detector import FoodDetector

app = Flask(__name__)
detector = FoodDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400
    
    food_description = data.get('food', '')
    
    if not food_description:
        return jsonify({'error': 'Please provide food description'}), 400
    
    result = detector.analyze_food(food_description)
    return jsonify(result)

if __name__ == '__main__':
    # Note: debug=True is for development only. 
    # For production deployment, use a WSGI server like gunicorn:
    # gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(debug=True, host='0.0.0.0', port=5000)
