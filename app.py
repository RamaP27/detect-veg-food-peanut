"""
Vegetarian Food Detection Application
A Flask web application for detecting vegetarian food items
"""
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Vegetarian food database (common vegetarian foods)
VEGETARIAN_FOODS = {
    'vegetables': ['broccoli', 'carrot', 'potato', 'tomato', 'spinach', 'lettuce', 
                   'cucumber', 'pepper', 'onion', 'garlic', 'cauliflower', 'cabbage',
                   'eggplant', 'zucchini', 'pumpkin', 'corn', 'peas', 'beans'],
    'fruits': ['apple', 'banana', 'orange', 'mango', 'strawberry', 'grape', 'watermelon',
               'pineapple', 'kiwi', 'peach', 'pear', 'plum', 'cherry', 'blueberry'],
    'grains': ['rice', 'bread', 'pasta', 'noodles', 'oats', 'quinoa', 'barley', 'wheat'],
    'dairy': ['cheese', 'milk', 'yogurt', 'butter', 'cream', 'paneer'],
    'legumes': ['lentils', 'chickpeas', 'tofu', 'tempeh', 'beans', 'peanuts'],
    'nuts': ['almond', 'walnut', 'cashew', 'pistachio', 'hazelnut', 'pecan'],
    'others': ['egg', 'salad', 'soup', 'pizza', 'burger', 'sandwich']
}

# Non-vegetarian food items
NON_VEGETARIAN_FOODS = [
    'chicken', 'beef', 'pork', 'mutton', 'lamb', 'fish', 'seafood', 'shrimp',
    'crab', 'lobster', 'prawn', 'salmon', 'tuna', 'turkey', 'duck', 'bacon',
    'sausage', 'ham', 'meat', 'steak'
]

# Peanut-containing foods
PEANUT_FOODS = ['peanut', 'peanut butter', 'groundnut', 'peanut oil', 'peanut sauce']


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def detect_food_type(food_name):
    """
    Detect if food is vegetarian and contains peanuts
    Returns: dict with detection results
    """
    food_name_lower = food_name.lower().strip()
    
    # Check for peanuts
    contains_peanut = any(peanut in food_name_lower for peanut in PEANUT_FOODS)
    
    # Check if non-vegetarian
    is_non_veg = any(non_veg in food_name_lower for non_veg in NON_VEGETARIAN_FOODS)
    
    # Check if vegetarian
    is_vegetarian = False
    food_category = None
    
    for category, foods in VEGETARIAN_FOODS.items():
        if any(food in food_name_lower for food in foods):
            is_vegetarian = True
            food_category = category
            break
    
    # If explicitly non-veg, mark as not vegetarian
    if is_non_veg:
        is_vegetarian = False
        food_category = 'non-vegetarian'
    
    return {
        'food_name': food_name,
        'is_vegetarian': is_vegetarian,
        'contains_peanut': contains_peanut,
        'category': food_category,
        'safe_for_veg': is_vegetarian and not is_non_veg,
        'allergen_warning': contains_peanut
    }


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    """Food detection page"""
    if request.method == 'POST':
        food_input = request.form.get('food_name', '').strip()
        
        if not food_input:
            flash('Please enter a food name', 'error')
            return redirect(url_for('detect'))
        
        # Detect food type
        result = detect_food_type(food_input)
        
        return render_template('result.html', result=result)
    
    return render_template('detect.html')


@app.route('/api/detect', methods=['POST'])
def api_detect():
    """API endpoint for food detection"""
    data = request.get_json()
    
    if not data or 'food_name' not in data:
        return jsonify({'error': 'Missing food_name parameter'}), 400
    
    food_name = data['food_name']
    result = detect_food_type(food_name)
    
    return jsonify(result)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Image upload page (placeholder for future ML integration)"""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            flash('Image uploaded successfully! (Image recognition coming soon)', 'success')
            return render_template('upload.html', uploaded=True, filename=filename)
        else:
            flash('Invalid file type. Please upload an image file.', 'error')
            return redirect(request.url)
    
    return render_template('upload.html', uploaded=False)


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404


@app.errorhandler(413)
def request_entity_too_large(error):
    """File too large error handler"""
    return 'File is too large. Maximum size is 16MB.', 413


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
