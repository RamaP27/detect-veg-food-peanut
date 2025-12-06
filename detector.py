import re


class FoodDetector:
    """Detects if food is vegetarian and if it contains peanuts."""
    
    # Non-vegetarian ingredients - class-level constants
    NON_VEG_KEYWORDS = [
        'meat', 'beef', 'pork', 'chicken', 'fish', 'salmon', 'tuna',
        'turkey', 'lamb', 'mutton', 'bacon', 'ham', 'sausage', 'shrimp',
        'prawn', 'crab', 'lobster', 'duck', 'goose', 'venison', 'seafood',
        'anchovy', 'anchovies', 'gelatin', 'gelatine'
    ]
    
    # Peanut-related keywords
    PEANUT_KEYWORDS = [
        'peanut', 'peanuts', 'groundnut', 'groundnuts', 'monkey nut',
        'monkey nuts', 'goober', 'goobers', 'peanut butter', 'peanut oil'
    ]
    
    def __init__(self):
        pass
    
    def analyze_food(self, food_description):
        """
        Analyze food description and return detection results.
        
        Args:
            food_description (str): Description of the food item
            
        Returns:
            dict: Results containing vegetarian status and peanut detection
        """
        food_lower = food_description.lower()
        
        # Check for non-vegetarian ingredients using word boundaries
        contains_non_veg = any(
            re.search(r'\b' + re.escape(keyword) + r'\b', food_lower)
            for keyword in self.NON_VEG_KEYWORDS
        )
        
        # Check for peanuts using word boundaries
        contains_peanuts = any(
            re.search(r'\b' + re.escape(keyword.replace(' ', r'\s+')) + r'\b', food_lower)
            for keyword in self.PEANUT_KEYWORDS
        )
        
        # Determine if vegetarian
        is_vegetarian = not contains_non_veg
        
        # Build result
        result = {
            'food': food_description,
            'is_vegetarian': is_vegetarian,
            'contains_peanuts': contains_peanuts,
            'vegetarian_status': 'Vegetarian' if is_vegetarian else 'Non-Vegetarian',
            'peanut_status': 'Contains Peanuts' if contains_peanuts else 'Peanut-Free',
            'warnings': []
        }
        
        # Add warnings
        if not is_vegetarian:
            result['warnings'].append('This food contains non-vegetarian ingredients.')
        
        if contains_peanuts:
            result['warnings'].append('⚠️ ALLERGEN WARNING: This food contains peanuts!')
        
        return result
