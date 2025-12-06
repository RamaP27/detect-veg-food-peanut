# 🥗 VegFood Detector - Vegetarian Food Detection App

A Flask-based web application for detecting vegetarian food items and identifying peanut allergens. This app helps vegetarians and people with peanut allergies make informed food choices.

## Features

- ✅ **Vegetarian Detection**: Instantly check if a food item is suitable for vegetarians
- 🥜 **Peanut Allergen Alert**: Get warnings about peanut content for allergy safety
- 🏷️ **Food Categorization**: Classify foods into categories (vegetables, fruits, grains, etc.)
- 📸 **Image Upload**: Upload food images (feature ready for future ML integration)
- 🌐 **RESTful API**: JSON API endpoint for programmatic access
- 💻 **Modern UI**: Clean, responsive interface that works on all devices

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/RamaP27/detect-veg-food-peanut.git
cd detect-veg-food-peanut
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

### Web Interface

1. **Home Page**: Overview of features and how the app works
2. **Detect Food**: Enter a food name to check if it's vegetarian and contains peanuts
3. **Upload Image**: Upload food images (placeholder for future ML integration)
4. **About**: Learn more about the application and its features

### API Usage

The application provides a RESTful API endpoint for programmatic access:

**Endpoint**: `POST /api/detect`

**Request**:
```bash
curl -X POST http://localhost:5000/api/detect \
  -H "Content-Type: application/json" \
  -d '{"food_name": "pizza"}'
```

**Response**:
```json
{
  "food_name": "pizza",
  "is_vegetarian": true,
  "contains_peanut": false,
  "category": "others",
  "safe_for_veg": true,
  "allergen_warning": false
}
```

## Food Detection Logic

The application checks food items against comprehensive databases:

### Vegetarian Categories
- **Vegetables**: broccoli, carrot, potato, tomato, spinach, etc.
- **Fruits**: apple, banana, orange, mango, strawberry, etc.
- **Grains**: rice, bread, pasta, noodles, oats, quinoa, etc.
- **Dairy**: cheese, milk, yogurt, butter, cream, paneer
- **Legumes**: lentils, chickpeas, tofu, tempeh, beans
- **Nuts**: almond, walnut, cashew, pistachio, etc.

### Non-Vegetarian Foods
Chicken, beef, pork, mutton, fish, seafood, and other meat products

### Peanut Detection
Identifies peanuts, peanut butter, groundnuts, peanut oil, and peanut sauce

## Project Structure

```
detect-veg-food-peanut/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── detect.html       # Detection form
│   ├── result.html       # Results page
│   ├── upload.html       # Image upload page
│   ├── about.html        # About page
│   └── 404.html          # 404 error page
├── static/               # Static files
│   └── css/
│       └── style.css     # Stylesheet
└── uploads/              # Uploaded images directory
```

## Configuration

You can configure the application by modifying these settings in `app.py`:

```python
app.config['UPLOAD_FOLDER'] = 'uploads'  # Upload directory
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size (16MB)
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}  # Allowed file types
```

## Future Enhancements

- 🤖 AI-powered image recognition using machine learning models
- 📊 Nutritional information display
- 🔍 Multi-food detection in one image
- 💾 User accounts and food history tracking
- 🌍 Multi-language support
- 📱 Mobile app development
- 🗄️ Expanded food database with regional cuisines

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This application provides general guidance based on common food ingredients. Always check food labels and consult with the food provider for accurate information about ingredients and allergens. This tool should not be used as a sole source for making dietary decisions, especially for people with severe allergies.

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please open an issue on GitHub.

---

**Original Reference**: https://ai.studio/apps/drive/12oaDKQ1PSt8ZdMSbe3ZkuOA5BoYiXkuC
