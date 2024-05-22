weather = {
    "Los Angeles": "Sunny",
    "New York": "Cloudy", 
    "Boston": "Cloudy",
}

sunny_cities = {key: value for (key, value) in weather.items() if value == "Sunny"}
print(sunny_cities)