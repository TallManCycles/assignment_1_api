import pytest
import math
import os
from models.LocationsClass import Location, ListOfLocations
from models.WeatherClass import Weather


def test_add_location():
    # create a new ListOfLocations object
    loc_list = ListOfLocations()

    # create a new Location object
    loc = Location("Paris", 48.8566, 2.3522)

    # add the location to the list
    loc_list.addLocation(loc)

    # check that the location was added to the list
    assert loc_list.getNumberOfLocations() == 1
    assert loc_list.getLocations()[0] == loc


def test_get_location_by_name():
    # create a new ListOfLocations object
    loc_list = ListOfLocations()

    # create two new Location objects
    loc1 = Location("Paris", 48.8566, 2.3522)
    loc2 = Location("New York", 40.7128, -74.0060)

    # add the locations to the list
    loc_list.addLocation(loc1)
    loc_list.addLocation(loc2)

    # check that we can retrieve the locations by name
    assert loc_list.getLocationByName("Paris") == loc1
    assert loc_list.getLocationByName("New York") == loc2
    assert loc_list.getLocationByName("London") is None


def test_remove_location():
    # create a new ListOfLocations object
    loc_list = ListOfLocations()

    # create two new Location objects
    loc1 = Location("Paris", 48.8566, 2.3522)
    loc2 = Location("New York", 40.7128, -74.0060)

    # add the locations to the list
    loc_list.addLocation(loc1)
    loc_list.addLocation(loc2)

    # remove one of the locations from the list
    loc_list.removeLocation(loc1)

    # check that the location was removed from the list
    assert loc_list.getNumberOfLocations() == 1
    assert loc_list.getLocations()[0] == loc2


def test_next_closest_location():
    # create a new ListOfLocations object
    loc_list = ListOfLocations()

    # create three new Location objects
    loc1 = Location("Paris", 48.8566, 2.3522)
    loc2 = Location("New York", 40.7128, -74.0060)
    loc3 = Location("Tokyo", 35.6895, 139.6917)

    # add the locations to the list
    loc_list.addLocation(loc1)
    loc_list.addLocation(loc2)
    loc_list.addLocation(loc3)

    # create a new Location object to use as the current location
    current_loc = Location("San Francisco", 37.7749, -122.4194)

    # check that the next closest location is correct
    assert loc_list.next_closest_location(current_loc) == loc2


def test_export_locations():
    # create a new ListOfLocations object
    loc_list = ListOfLocations()

    testData = {
        "coord": {
            "lon": 2.3522,
            "lat": 48.8566
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 280.32,
            "feels_like": 278.37,
            "temp_min": 279.82,
            "temp_max": 281.48,
            "pressure": 1023,
            "humidity": 100
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.5,
            "deg": 350
        },
        "clouds": {
            "all": 0
        },
        "dt": 1603110647,
        "sys": {
            "type": 1,
            "id": 6550,
            "country": "FR",
            "sunrise": 1603070303,
            "sunset": 1603111990
        },
        "timezone": 7200,
        "id": 2988507,
        "name": "Test Location",
        "cod": 200
    }

    # create three new Location objects
    loc1 = Location("Paris", 48.8566, 2.3522)
    loc1.current_weather = Weather(testData)
    loc2 = Location("New York", 40.7128, -74.0060)
    loc2.current_weather = Weather(testData)
    loc3 = Location("Tokyo", 35.6895, 139.6917)
    loc3.current_weather = Weather(testData)

    # add the locations to the list
    loc_list.addLocation(loc1)
    loc_list.addLocation(loc2)
    loc_list.addLocation(loc3)

    # export the locations to a file
    loc_list.exportLocations("locations.txt")

    # check that the file was created
    assert os.path.exists("locations.txt")

    # check that the file contains the correct data
    with open("locations.txt", "r") as f:
        lines = f.readlines()
        assert len(lines) == 3