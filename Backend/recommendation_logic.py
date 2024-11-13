import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample restaurant data with attributes for each restaurant
restaurants = {
    "restaurant1": [1, 30, 4.5, 90],  # [cuisine type, avg price, rating, popularity]
    "restaurant2": [2, 50, 4.0, 70],  #  need more data and store this data in csv or json format 
    "restaurant3": [1, 40, 4.7, 80],
    "restaurant4": [3, 25, 4.3, 60],
    "restaurant5": [2, 35, 4.1, 85]
}

# Convert restaurant data into arrays
restaurant_names = list(restaurants.keys())
restaurant_vectors = np.array(list(restaurants.values()))

# Track likes and dislikes for each user
user_swipes = {
    "User1": {"liked": [], "disliked": []},
    "User2": {"liked": [], "disliked": []}
} # need to store this in csv format 

def swipe_restaurant(user, restaurant_name, action):
    """Records swipe action (like or dislike) for a user on a specific restaurant."""
    if action == "r":
        user_swipes[user]["liked"].append(restaurant_name)
    elif action == "l":
        user_swipes[user]["disliked"].append(restaurant_name)
    return f"{user} swiped {'right' if action == 'r' else 'left'} on {restaurant_name}"

def get_recommendations_for_couple():
    """Generates restaurant recommendations based on both users' liked restaurants."""
    # Get liked restaurants from both users
    user1_likes = user_swipes["User1"]["liked"]
    user2_likes = user_swipes["User2"]["liked"]
    
    # Find common liked restaurants
    common_likes = set(user1_likes) & set(user2_likes)
    if common_likes:
        return [{"name": rest, "similarity_score": 1.0} for rest in common_likes]
    
    # Calculate average preference vectors for each user
    def get_avg_vector(user_likes):
        indices = [restaurant_names.index(rest) for rest in user_likes]
        vectors = restaurant_vectors[indices]
        return np.mean(vectors, axis=0) if len(vectors) > 0 else np.zeros(restaurant_vectors.shape[1])

    avg_user1_vector = get_avg_vector(user1_likes)
    avg_user2_vector = get_avg_vector(user2_likes)
    
    # Combine preferences and calculate similarity to all restaurants
    combined_vector = (avg_user1_vector + avg_user2_vector) / 2
    similarity_scores = cosine_similarity(combined_vector.reshape(1, -1), restaurant_vectors).flatten()
    
    # Sort restaurants by similarity score, filtering out already swiped ones
    sorted_indices = np.argsort(similarity_scores)[::-1]
    recommendations = [
        {"name": restaurant_names[i], "similarity_score": similarity_scores[i]}
        for i in sorted_indices
        if restaurant_names[i] not in user1_likes + user2_likes + user_swipes["User1"]["disliked"] + user_swipes["User2"]["disliked"]
    ]
    
    return recommendations[:3]  # Return top 3 recommendations
