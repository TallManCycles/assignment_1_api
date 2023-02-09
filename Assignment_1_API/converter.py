
# Converts the temperature from Kelvin to Celsius
def kelvin_to_celsius(kelvin_temp: float) -> float:
    # Returns:
    # temperature in Celsius
    # parse the temperature from Kelvin to Celsius and return with two decimal places
    return round(kelvin_temp - 273.15, 2)
