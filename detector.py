class FoodDetector:
    """Detects if food is vegetarian and if it contains peanuts."""
    
    def __init__(self):
        # Non-vegetarian ingredients
        self.non_veg_keywords = [
            'meat', 'beef', 'pork', 'chicken', 'fish', 'salmon', 'tuna',
            'turkey', 'lamb', 'mutton', 'bacon', 'ham', 'sausage', 'shrimp',
            'prawn', 'crab', 'lobster', 'duck', 'goose', 'venison', 'seafood',
            'anchovy', 'anchovies', 'gelatin', 'gelatine'
        ]
        
        # Peanut-related keywords
        self.peanut_keywords = [
            'peanut', 'peanuts', 'groundnut', 'groundnuts', 'monkey nut',
            'monkey nuts', 'goober', 'goobers', 'peanut butter', 'peanut oil'
        ]
        
        # Vegetarian indicators
        self.veg_keywords = [
            'vegetable', 'vegetables', 'vegan', 'vegetarian', 'plant-based',
            'salad', 'fruit', 'fruits', 'tofu', 'beans', 'lentils', 'rice',
            'pasta', 'bread', 'cheese', 'paneer', 'dal', 'quinoa'
        ]
    
    def analyze_food(self, food_description):
        """
        Analyze food description and return detection results.
        
        Args:
            food_description (str): Description of the food item
            
        Returns:
            dict: Results containing vegetarian status and peanut detection
        """
        food_lower = food_description.lower()
        
        # Check for non-vegetarian ingredients
        contains_non_veg = any(keyword in food_lower for keyword in self.non_veg_keywords)
        
        # Check for peanuts
        contains_peanuts = any(keyword in food_lower for keyword in self.peanut_keywords)
        
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
