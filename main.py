import requests
import json
import Assignment_1_API.models.LocationsClass as Locations
import Assignment_1_API.models.OpenWeather as OpenWeather
import threading
import time

"""
This program will load the travel locations from the server and display them to the user.
The user will then be able to select a location and add it to their itinerary.
The user will then be able to view their itinerary and export it to a text file.
"""

# creates a blank list of locations
travel_locations = Locations.ListOfLocations()

# A decorator to check that the user has loaded the locations
def check_locations_loaded(func):
    def wrapper(*args, **kwargs):
        if travel_locations.getNumberOfLocations() == 0:
            print("Please load the locations first.")
        else:
            func(*args, **kwargs)

    return wrapper


# Loads the locations and weather from the server
def load_locations():
    # url to get the travel locations from
    try:
        response = requests.get("http://127.0.0.1:8000/app/load_locations/")
    except requests.exceptions.ConnectionError:
        print("Error connecting to server. Please ensure the API server is running.")
        return

    # if the response is successful
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

        print("\rloaded locations successfully!     ")

    else:
        print("Error loading locations")

# Creates a thread to load the locations asynchronously
def create_thread():
    global i
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


# prints all locations and weather descriptions
@check_locations_loaded
def print_locations():
    global i, location
    # ask for input as an integer, and list all locations and weather descriptions

    for i in range(travel_locations.getNumberOfLocations()):
        location = travel_locations.getLocation(i)
        print(f'{i} - {location.name} - {location.current_weather.weather_description}')


# exports the locations to a text file
def export_locations():
    new_travel_locations.exportLocations('itinerary.csv')
    print("Your list has been exported successfully!")


# shows the itinerary
def show_itinerary():
    global i, location
    print("Your current itinerary is:")
    for i in range(new_travel_locations.getNumberOfLocations()):
        location = new_travel_locations.getLocation(i)
        print(f'{location.name} - {location.current_weather.weather_description}')


print("Welcome to the Travel App! This app will help you plan your next trip!")
print("Loading travel locations, please wait...")

# load the locations
create_thread()

exit_program = False


def closest_location_selection():
    next_location = 'y'
    while next_location == 'y':
        closest_location = travel_locations.next_closest_location(
            new_travel_locations.getLocation(new_travel_locations.getNumberOfLocations() - 1))

        # check if closest_location is empty
        if closest_location.name == '':
            break

        next_location = input(
            f"The closest location to your current location is {closest_location.name}. Would you like to go there next? (y/n)")
        if next_location == 'y':
            new_travel_locations.addLocation(closest_location)

            if travel_locations.containsLocation(closest_location):
                travel_locations.removeLocation(closest_location)

            print("Great choice! I like your style!")
        else:
            print("Okay, we'll continue.")


def weather_location_selection():
    next_location = 'y'
    while next_location == 'y':
        best_location = travel_locations.getBestWeather()

        # check if location is empty
        if best_location.name == '':
            break

        next_location = input(
            f"The next best weather is {best_location.name}. Would you like to go there next? (y/n)")
        if next_location == 'y':
            new_travel_locations.addLocation(best_location)

            if travel_locations.containsLocation(best_location):
                travel_locations.removeLocation(best_location)

            print("Great choice! I like your style!")
        else:
            print("Okay, we'll continue.")


while not exit_program:

    print_locations()

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

        print_locations()

        proximity_or_weather = input(
            "Would you like to select the next location by proximity or weather? (p/w): ")

        if proximity_or_weather == 'p':
            closest_location_selection()
        else:
            weather_location_selection()

    if new_travel_locations.getNumberOfLocations() != 0:
        show_itinery = input('Would you like to see your current itinerary? (y/n)')
        if show_itinery == 'y':
            show_itinerary()

        export_itinerary = input('Would you like to export your itinerary for GPS Navigation? (y/n)')
        if export_itinerary == 'y':
            export_locations()
        else:
            print("Okay, we'll continue.")

    # ask if the user would like to end the program
    user_input = input("Would you like to exit the program? (y/n): ")

    if user_input == "y":
        exit_program = True
    else:
        exit_program = False



