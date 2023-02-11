import pytest
import math
from models.LocationsClass import Location, ListOfLocations


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
