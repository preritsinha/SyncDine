import SwiftUI

struct ContentView: View {
    @State private var restaurants = [Restaurant]()
    @State private var likedRestaurants = [Restaurant]()
    private let apiManager = APIManager()

    var body: some View {
        ZStack {
            ForEach(restaurants) { restaurant in
                RestaurantCardView(restaurant: restaurant)
                    .gesture(DragGesture()
                        .onEnded { drag in
                            if drag.translation.width > 100 {
                                swipeRight(restaurant: restaurant)
                            } else if drag.translation.width < -100 {
                                swipeLeft(restaurant: restaurant)
                            }
                        })
            }
        }
        .onAppear(perform: loadRestaurants)
    }
    
    func swipeRight(restaurant: Restaurant) {
        likedRestaurants.append(restaurant)
        apiManager.swipeRestaurant(user: "User1", restaurant: restaurant.name, action: "r")
        removeRestaurant(restaurant)
    }
    
    func swipeLeft(restaurant: Restaurant) {
        apiManager.swipeRestaurant(user: "User1", restaurant: restaurant.name, action: "l")
        removeRestaurant(restaurant)
    }

    func removeRestaurant(_ restaurant: Restaurant) {
        restaurants.removeAll { $0.id == restaurant.id }
    }
    
    func loadRestaurants() {
        // Sample static restaurants for now
        restaurants = [
            Restaurant(name: "Restaurant A", cuisineType: "Italian", rating: 4.5, averagePrice: 20),
            Restaurant(name: "Restaurant B", cuisineType: "Japanese", rating: 4.0, averagePrice: 30),
            // Add more restaurants or load from API
        ]
    }
}
