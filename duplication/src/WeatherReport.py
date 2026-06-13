class Forecast:
    def __init__(self, period, temperature, condition, wind_speed):
        self.period = period  # "morning", "afternoon", "evening", "night"
        self.temperature = temperature
        self.condition = condition
        self.wind_speed = wind_speed

    def is_morning(self):
        return self.period == "morning"

    def is_afternoon(self):
        return self.period == "afternoon"

    def is_evening(self):
        return self.period == "evening"

    def is_night(self):
        return self.period == "night"

    def get_temperature(self):
        return self.temperature

    def get_condition(self):
        return self.condition

    def get_wind_speed(self):
        return self.wind_speed


class WeatherReport:
    def format_daily_report(self, forecasts, output):
        for forecast in forecasts:

            if forecast.is_morning():
                line = (
                    "Morning: "
                    + str(forecast.get_temperature())
                    + "°C, "
                    + forecast.get_condition()
                    + ", wind "
                    + str(forecast.get_wind_speed())
                    + "km/h"
                )
                output.append(line)

            if forecast.is_afternoon():
                line = (
                    "Afternoon: "
                    + str(forecast.get_temperature())
                    + "°C, "
                    + forecast.get_condition()
                    + ", wind "
                    + str(forecast.get_wind_speed())
                    + "km/h"
                )
                output.append(line)

            if forecast.is_evening():
                line = (
                    "Evening: "
                    + str(forecast.get_temperature())
                    + "°C, "
                    + forecast.get_condition()
                    + ", wind "
                    + str(forecast.get_wind_speed())
                    + "km/h"
                )
                output.append(line)

            if forecast.is_night():
                line = (
                    "Night: "
                    + str(forecast.get_temperature())
                    + "°C, "
                    + forecast.get_condition()
                    + ", wind "
                    + str(forecast.get_wind_speed())
                    + "km/h"
                )
                output.append(line)