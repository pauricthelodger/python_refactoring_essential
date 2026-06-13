import unittest

from duplication.src.WeatherReport import WeatherReport, Forecast


class WeatherReportTest(unittest.TestCase):

    def test_formats_morning_forecast_correctly(self):
        report = WeatherReport()

        forecast = Forecast("morning", 12.5, "Cloudy", 10)

        output = []
        report.format_daily_report([forecast], output)

        self.assertEqual(1, len(output))
        self.assertEqual(
            "Morning: 12.5°C, Cloudy, wind 10km/h",
            output[0]
        )

    def test_formats_afternoon_forecast_correctly(self):
        report = WeatherReport()

        forecast = Forecast("afternoon", 8.0, "Rain", 20)

        output = []
        report.format_daily_report([forecast], output)

        self.assertEqual(1, len(output))
        self.assertEqual(
            "Afternoon: 8.0°C, Rain, wind 20km/h",
            output[0]
        )

    def test_formats_evening_forecast_correctly(self):
        report = WeatherReport()

        forecast = Forecast("evening", 8.0, "Rain", 20)

        output = []
        report.format_daily_report([forecast], output)

        self.assertEqual(1, len(output))
        self.assertEqual(
            "Evening: 8.0°C, Rain, wind 20km/h",
            output[0]
        )

    def test_formats_multiple_forecasts_in_order(self):
        report = WeatherReport()

        forecasts = [
            Forecast("morning", 10.0, "Sunny", 5),
            Forecast("night", 3.0, "Clear", 2)
        ]

        output = []
        report.format_daily_report(forecasts, output)

        self.assertEqual(2, len(output))

        self.assertEqual(
            "Morning: 10.0°C, Sunny, wind 5km/h",
            output[0]
        )

        self.assertEqual(
            "Night: 3.0°C, Clear, wind 2km/h",
            output[1]
        )


if __name__ == "__main__":
    unittest.main()