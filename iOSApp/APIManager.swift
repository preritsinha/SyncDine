import Foundation

class APIManager {
    func swipeRestaurant(user: String, restaurant: String, action: String) {
        let url = URL(string: "http://localhost:5000/swipe")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let body: [String: Any] = ["user": user, "restaurant_name": restaurant, "action": action]
        request.httpBody = try? JSONSerialization.data(withJSONObject: body)

        URLSession.shared.dataTask(with: request) { data, response, error in
            if let data = data {
                let response = try? JSONDecoder().decode([String: String].self, from: data)
                print(response?["status"] ?? "No response")
            }
        }.resume()
    }
    
    func fetchRecommendations(completion: @escaping ([Restaurant]) -> Void) {
        let url = URL(string: "http://localhost:5000/recommend")!
        
        URLSession.shared.dataTask(with: url) { data, response, error in
            if let data = data {
                let recommendations = try? JSONDecoder().decode([Restaurant].self, from: data)
                DispatchQueue.main.async {
                    completion(recommendations ?? [])
                }
            }
        }.resume()
    }
}
