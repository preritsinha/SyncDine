import Foundation

class Networking {
    func swipe(user: String, restaurantName: String, action: String, completion: @escaping (Result<String, Error>) -> Void) {
        let url = URL(string: "http://127.0.0.1:5000/swipe")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        let payload: [String: Any] = [
            "user": user,
            "restaurant_name": restaurantName,
            "action": action
        ]

        request.httpBody = try? JSONSerialization.data(withJSONObject: payload)

        URLSession.shared.dataTask(with: request) { data, _, error in
            if let error = error {
                completion(.failure(error))
            } else if let data = data, let response = String(data: data, encoding: .utf8) {
                completion(.success(response))
            }
        }.resume()
    }
}
