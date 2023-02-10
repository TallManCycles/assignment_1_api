class Weather:
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
