import requests
import json
import Assignment_1_API.models.LocationsClass as Locations
import Assignment_1_API.models.OpenWeather as OpenWeather
import threading
import time

# creates a blank list of locations
travel_locations = Locations.ListOfLocations()


def load_locations():
    # url to get the travel locations from
    response = requests.get("http://127.0.0.1:8000/app/load_locations/")

    if response.status_code == 200:
        locations = json.loads(response.content)

        for location in locations:
            new_location = Locations.Location(location['name'], location['latitude'], location['longitude'])
            travel_locations.addLocation(new_location)

        # add the location weather to the location object
        for location in travel_locations.getLocations():
            weather = OpenWeather.getWeatherByCoordinates(location.lat, location.lon)

            # if weather is of type Weather
            if isinstance(weather, OpenWeather.Weather):
                location.current_weather = weather
            else:
                location.current_weather = "weather not found"

print("Welcome to the Travel App! This app will help you plan your next trip!")
print("Loading travel locations, please wait...")

# Start the loading process in a separate thread
thread = threading.Thread(target=load_locations)
thread.start()

# Show the loading message
loading_chars = ["-", "\\", "|", "/"]
i = 0
while thread.is_alive():
    print(f"\rLoading locations... {loading_chars[i % len(loading_chars)]}", end="")
    i += 1
    time.sleep(0.2)

print("\rData locations successfully!     ")

exit_program = False

while not exit_program:

    # ask for input as an integer, and list all locations and weather descriptions
    for i in range(travel_locations.getNumberOfLocations()):
        location = travel_locations.getLocation(i)
        print(f'{i} - {location.name} - {location.current_weather.weather_description}')


    new_travel_locations = Locations.ListOfLocations()


    while travel_locations.getNumberOfLocations() > 0:

        while True:
            try:
                user_input = int(input("Please enter the number of the location you would like to visit: "))
                if user_input > travel_locations.getNumberOfLocations():
                    print("Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        current_location = travel_locations.getLocation(user_input)

        new_travel_locations.addLocation(current_location)
        travel_locations.removeLocation(current_location)

        print("Nice! I like your style!")


        for i in range(travel_locations.getNumberOfLocations()):
            if i == 0:
                print("Here are the remaining locations:")
            location = travel_locations.getLocation(i)
            print(f'{i} - {location.name} - {location.current_weather.weather_description}')

        next_location = 'y'

        while next_location == 'y':
            closest_location = travel_locations.next_closest_location(
                new_travel_locations.getLocation(new_travel_locations.getNumberOfLocations() - 1))

            # check if closest_location is empty
            if closest_location.name == '':
                break

            next_location = input(f"The closest location to your current location is {closest_location.name}. Would you like to go there next? (y/n)")
            if next_location == 'y':
                new_travel_locations.addLocation(closest_location)

                if travel_locations.containsLocation(closest_location):
                    travel_locations.removeLocation(closest_location)

                print("Great choice! I like your style!")
            else:
                print("Okay, we'll continue.")


    show_itinery = input('Would you like to see your current itinerary? (y/n)')
    if show_itinery == 'y':
        print("Your current itinerary is:")
        for i in range(new_travel_locations.getNumberOfLocations()):
            location = new_travel_locations.getLocation(i)
            print(f'{location.name} - {location.current_weather.weather_description}')
    else:
        print("Okay, we'll continue.")

    # ask if the user would like to end the program
    user_input = input("Would you like to exit the program? (y/n): ")

    if user_input == "y":
        exit_program = True
    else:
        exit_program = False
