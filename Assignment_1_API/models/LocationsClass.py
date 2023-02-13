import math

class Location:
    def __init__(self, name, lat, lon, current_weather=None):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.current_weather = current_weather


# Create a class that holds a list of locations
class ListOfLocations:
    def __init__(self):
        self.locations = []

#     # Add a location to the list
    def addLocation(self, location):
        self.locations.append(location)

#     # Return the list of locations
    def getLocations(self):
        return self.locations

#     # Return the location at the specified index
    def getLocation(self, index):
        return self.locations[index]

#     # Return the number of locations in the list
    def getNumberOfLocations(self):
        return len(self.locations)

#     # Return the location with the specified name
    def getLocationByName(self, name):
        for location in self.locations:
            if location.name == name:
                return location
        return None

#     # Return the location with the specified coordinates
    def getLocationByCoordinates(self, lat, lon):
        for location in self.locations:
            if location.lat == lat and location.lon == lon:
                return location
        return None

#     returns true if the location is in the list
    def containsLocation(self, location):
        for l in self.locations:
            if l.name == location.name:
                return True
        return False

#     remove a location from the list
    def removeLocation(self, location):
        self.locations.remove(location)

    # Return the closes location to the specified location
    def next_closest_location(self, current_location):
        closest_location = Location("", 0, 0)
        closest_distance = float('inf')
        for location in self.locations:
            lat1, lon1 = current_location.lat, current_location.lon
            lat2, lon2 = location.lat, location.lon
            distance = math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)
            if distance < closest_distance:
                closest_distance = distance
                closest_location = location

        return closest_location

    # Export the list of locations to a file
    def exportLocations(self, filename):
        with open(filename, 'w') as file:
            for location in self.locations:
                file.write(f'{location.name},{location.lat},{location.lon}\n')


#     Get the location with the best weather from the list
    def getBestWeather(self):
        best_weather = self.locations[0].current_weather
        for location in self.locations:
            if location.current_weather.temp > best_weather.temp:
                best_weather = location.current_weather
        return best_weather

