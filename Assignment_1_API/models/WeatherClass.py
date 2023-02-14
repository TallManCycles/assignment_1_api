class Weather:
    """
    Create a class that holds the weather data for a location

    Attributes:
        coordinates (dict): The coordinates of the location
        weather (dict): The weather at the location
        weather_main (str): The main weather at the location
        weather_description (str): The description of the weather at the location
        temp (float): The temperature at the location
        feels_like (float): The temperature at the location that it feels like
        temp_min (float): The minimum temperature at the location
        temp_max (float): The maximum temperature at the location
        pressure (int): The pressure at the location
        humidity (int): The humidity at the location
        visibility (int): The visibility at the location
        wind (dict): The wind at the location
        rain (dict): The rain at the location
        clouds (dict): The clouds at the location
        timezone (int): The timezone at the location
        name: The name of the location

    Functions:
        __init__ (self, data): The constructor for the Weather class

    """
    def __init__(self, data):
        if data:
            self.coordinates = data["coord"]
            self.weather = data["weather"][0]
            # Group of weather parameters (Rain, Snow, Extreme etc.)
            self.weather_main = data["weather"][0]["main"]
            self.weather_description = data["weather"][0]["description"]
            self.temp = data["main"]["temp"]
            self.feels_like = data["main"]["feels_like"]
            self.temp_min = data["main"]["temp_min"]
            self.temp_max = data["main"]["temp_max"]
            self.pressure = data["main"]["pressure"]
            self.humidity = data["main"]["humidity"]
            self.visibility = data["visibility"]
            self.wind = data["wind"]
            self.rain = data.get("rain", {})
            self.clouds = data["clouds"]
            self.timezone = data["timezone"]
            self.name = data["name"]
        else:
            self.coordinates = None
            self.weather = None
            self.weather_main = None
            self.weather_description = None
            self.temp = None
            self.feels_like = None
            self.temp_min = None
            self.temp_max = None
            self.pressure = None
            self.humidity = None
            self.visibility = None
            self.wind = None
            self.rain = None
            self.clouds = None
            self.timezone = None
            self.name = None
