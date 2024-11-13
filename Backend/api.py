from flask import Flask, request, jsonify
from recommendation_logic import swipe_restaurant, get_recommendations_for_couple

app = Flask(__name__)

@app.route('/swipe', methods=['POST'])
def swipe():
    """Handles swipe actions for each user on a specific restaurant."""
    data = request.json
    user = data.get("user")
    restaurant_name = data.get("restaurant_name")
    action = data.get("action")
    
    if user and restaurant_name and action in ("r", "l"):
        result = swipe_restaurant(user, restaurant_name, action)
        return jsonify({"status": "success", "result": result})
    else:
        return jsonify({"status": "error", "message": "Invalid input"}), 400

@app.route('/recommend', methods=['GET'])
def recommend():
    """Provides restaurant recommendations based on swipes from both users."""
    recommendations = get_recommendations_for_couple()
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
