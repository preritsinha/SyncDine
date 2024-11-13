import Foundation

struct Restaurant: Identifiable, Codable {
    let id = UUID()
    var name: String
    var cuisineType: String
    var rating: Double
    var averagePrice: Double

    static let example = Restaurant(name: "Sample Restaurant", cuisineType: "Italian", rating: 4.5, averagePrice: 30)
}
