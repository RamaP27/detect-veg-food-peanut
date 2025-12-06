# 🥗 Vegetarian Food & Peanut Detector

A simple web application that helps identify whether food items are vegetarian and detects the presence of peanuts for allergen warnings.

## Features

- **Vegetarian Detection**: Identifies if food contains non-vegetarian ingredients
- **Peanut Allergen Detection**: Detects peanut ingredients for allergen warnings
- **User-Friendly Interface**: Clean, modern web interface
- **Real-Time Analysis**: Instant feedback on food descriptions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/RamaP27/detect-veg-food-peanut.git
cd detect-veg-food-peanut
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Development Mode

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

### Production Deployment

For production, use a WSGI server like gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. Enter a food description or list of ingredients and click "Analyze Food"

## Examples

Try these examples:
- "Grilled chicken salad" → Non-Vegetarian
- "Vegetable curry with tofu" → Vegetarian, Peanut-Free
- "Peanut butter sandwich" → Vegetarian, Contains Peanuts
- "Beef stir-fry with peanuts" → Non-Vegetarian, Contains Peanuts

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Detection**: Keyword-based analysis

## How It Works

The application uses keyword matching to:
1. Scan food descriptions for non-vegetarian ingredients (meat, fish, etc.)
2. Detect peanut-related terms (peanuts, peanut butter, etc.)
3. Provide clear feedback with warnings for allergens

## Project Structure

```
detect-veg-food-peanut/
├── app.py              # Flask application
├── detector.py         # Food detection logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
└── README.md          # Documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
