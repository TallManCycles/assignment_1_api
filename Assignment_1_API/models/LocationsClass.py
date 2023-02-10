
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

#     remove a location from the list
    def removeLocation(self, location):
        self.locations.remove(location)