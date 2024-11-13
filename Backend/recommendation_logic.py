from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class RecommendationLogic:
    def __init__(self):
        self.user_swipes = {}
        self.restaurant_features = {
            'restaurant1': [1, 0, 1, 0],
            'restaurant2': [0, 1, 1, 0],
            'restaurant3': [1, 1, 0, 1]
        }

    def handle_swipe(self, user, restaurant_name, action):
        if user not in self.user_swipes:
            self.user_swipes[user] = {}
        self.user_swipes[user][restaurant_name] = action
        return f"{user} swiped {'right' if action == 'r' else 'left'} on {restaurant_name}"

    def get_recommendations(self):
        user_vector = np.array([1, 0, 0, 1])
        restaurant_vectors = np.array(list(self.restaurant_features.values()))
        similarities = cosine_similarity([user_vector], restaurant_vectors)[0]
        sorted_indices = similarities.argsort()[::-1]
        sorted_restaurants = [
            {"name": list(self.restaurant_features.keys())[i], "similarity_score": similarities[i]}
            for i in sorted_indices
        ]
        return sorted_restaurants[:3]
