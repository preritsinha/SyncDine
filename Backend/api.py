from flask import Flask, request, jsonify
from recommendation_logic import RecommendationLogic

app = Flask(__name__)
recommendation_logic = RecommendationLogic()

@app.route('/swipe', methods=['POST'])
def swipe():
    data = request.get_json()
    user = data.get('user')
    restaurant_name = data.get('restaurant_name')
    action = data.get('action')

    result = recommendation_logic.handle_swipe(user, restaurant_name, action)
    return jsonify({"status": "success", "result": result})

@app.route('/recommend', methods=['GET'])
def recommend():
    recommendations = recommendation_logic.get_recommendations()
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
