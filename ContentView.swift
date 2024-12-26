import SwiftUI

struct ContentView: View {
    let networking = Networking()

    var body: some View {
        VStack {
            Text("Welcome to DineMatch!")
                .font(.title)
                .padding()

            Button(action: {
                networking.swipe(user: "User1", restaurantName: "restaurant1", action: "r") { result in
                    switch result {
                    case .success(let response):
                        print(response)
                    case .failure(let error):
                        print("Error: \(error)")
                    }
                }
            }) {
                Text("Swipe Restaurant")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
        }
    }
}
