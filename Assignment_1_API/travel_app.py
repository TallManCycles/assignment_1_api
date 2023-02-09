import OpenWeather as OpenWeather
import Locations
import converter
import time
import sys
import threading
import time

# Creates a new list of locations object
travel_locations = Locations.ListOfLocations()


def load_locations():
    travel_locations.addLocation(Locations.Location(
        'Palm Beach', 26.7056, -80.0364))
    travel_locations.addLocation(Locations.Location(
        'Lake District National Park', 54.4609, 3.0886))
    travel_locations.addLocation(Locations.Location(
        'Corfe Castle', 50.6395, 2.0566))
    travel_locations.addLocation(Locations.Location(
        'The Cotswolds', 51.8330, 1.8433))
    travel_locations.addLocation(Locations.Location(
        'Cambridge', 52.2053, 0.1218))
    travel_locations.addLocation(Locations.Location(
        'Bristol', 51.4545, 2.5879))
    travel_locations.addLocation(Locations.Location(
        'Oxford', 51.7520, 1.257))
    travel_locations.addLocation(Locations.Location(
        'Norwich', 52.6309, 1.2974))
    travel_locations.addLocation(Locations.Location(
        'Stonehenge', 51.1789, 1.8262))
    travel_locations.addLocation(Locations.Location(
        'Watergate Bay', 50.4429, 5.0553))
    travel_locations.addLocation(Locations.Location(
        'Birmingham', 52.4862, 1.8904))

    # add the location weather to the location object
    for location in travel_locations.getLocations():
        weather = OpenWeather.getWeatherByCoordinates(location.lat, location.lon)

        # if weather is of type Weather
        if isinstance(weather, OpenWeather.Weather):
            location.current_weather = weather
        else:
            location.current_weather = "weather not found"


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

    user_input = int(input("Please enter the number of the location you would like to visit first: "))

    # create a new list of locations, and add the location the user selected to the top of the list
    new_travel_locations = Locations.ListOfLocations()

    new_travel_locations.addLocation(travel_locations.getLocation(user_input))
    travel_locations.removeLocation(travel_locations.getLocation(user_input))

    print("Nice! I like your style!")

    while travel_locations.getNumberOfLocations() > 0:

        user_input = int(input("Please enter the number of the location you would like to visit next: "))

        if user_input > travel_locations.getNumberOfLocations():
            print("Please enter a valid number.")
            user_input = int(input("Please enter the number of the location you would like to visit next: "))
            continue

        new_travel_locations.addLocation(travel_locations.getLocation(user_input))
        travel_locations.removeLocation(travel_locations.getLocation(user_input))

        print("Great choice! I like your style!")

        for i in range(travel_locations.getNumberOfLocations()):
            location = travel_locations.getLocation(i)
            print(f'{i} - {location.name} - {location.current_weather.weather_description}')

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
