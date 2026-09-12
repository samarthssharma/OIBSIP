import requests

print("Welcome to the Weather App")
print("--------------------------")

# Paste your API key inside the quotes below
API_KEY = "ed6e7ef3f251f208a418e67b4058b273"

while True:
    # 1. Ask user for a city and reject empty input
    city = input("\nEnter a city name (or type 'quit' to exit): ").strip()
    
    if city.lower() == 'quit':
        print("Goodbye!")
        break
        
    if city == "":
        print("Error: You cannot leave the city name blank. Try again.")
        continue

    # 2. Set up the API URL (asking for metric units so we get Celsius)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        # 3. Make the API call to get the data
        response = requests.get(url)
        data = response.json()

        # 4. Handle API Errors gracefully
        if response.status_code == 401:
            print("Error: Invalid API Key. Make sure you pasted it correctly in the code.")
            break
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found. Please check the spelling.")
            continue
        elif response.status_code != 200:
            print("Error: Something went wrong with the weather service.")
            continue

        # 5. Extract the specific data we need from the JSON response
        temp_celsius = data["main"]["temp"]
        # Convert Celsius to Fahrenheit using basic math
        temp_fahrenheit = (temp_celsius * 9/5) + 32 
        
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # 6. Display the results nicely
        print(f"\n--- Current Weather in {data['name']} ---")
        print(f"Condition: {weather_desc.title()}")
        print(f"Temperature: {temp_celsius}°C ({temp_fahrenheit:.1f}°F)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} meters/sec")
        print("---------------------------------")

    except requests.exceptions.RequestException:
        # This catches network timeouts or if your laptop loses internet connection
        print("Error: Could not connect to the internet. Please check your connection.")