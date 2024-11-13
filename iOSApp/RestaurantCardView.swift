import SwiftUI

struct RestaurantCardView: View {
    var restaurant: Restaurant
    
    var body: some View {
        VStack {
            Text(restaurant.name)
                .font(.title)
            Text("Cuisine: \(restaurant.cuisineType)")
            Text("Rating: \(restaurant.rating)")
            Text("Price: \(restaurant.averagePrice)")
        }
        .padding()
        .background(Color.white)
        .cornerRadius(10)
        .shadow(radius: 5)
    }
}

struct RestaurantCardView_Previews: PreviewProvider {
    static var previews: some View {
        RestaurantCardView(restaurant: Restaurant.example)
    }
}
