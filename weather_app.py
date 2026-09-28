import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()    
        self.city_label = QLabel("Enter City Name: " , self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel( self)
        self.desctiption_label=QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desctiption_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter) 
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desctiption_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input") 
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.desctiption_label.setObjectName("desctiption_label")

        self.setStyleSheet("""
            QLabel  , QPushButton {
            
                font-family : calibri;
            }

            QLabel#city_label {
                font-size: 40px;
                font-style: italic;

            }

            QLineEdit#city_input {
                font-size: 50px;
            }

            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }

            QLabel#temperature_label {
                font-size: 75px;
                font-weight: bold;
            }
            QLabel#emoji_label {
                font-size: 90px;
                font-family: Segoe UI Emoji ;
            }
            QLabel#desctiption_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "6522a6cecbdc0f1a82e6e6e9efe88ac0"
        city= self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError:
            match response.status_code:
                case 404:
                    self.display_error("City not found.")
                case 401:
                    self.display_error("Invalid API key.")
                case _:
                    self.display_error("An error occurred while fetching weather data.")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\n Please check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\n Please try again later.")
        except requests.exceptions.TooManyRedirects:
            self.display_error ("Too Many Redirects Error\n Please try again later.")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Exception: {req_error}")
        


    def display_error(self , message):
        self.temperature_label.setStyleSheet("font-size : 30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.desctiption_label.clear()

    def display_weather(self, data):
        temperature_c = data["main"]["temp"]
        self.temperature_label.setText(f"{temperature_c:.1f}°C")
        self.temperature_label.setStyleSheet("font-size: 75px")

        weather_id= data["weather"][0]["id"]
        weather_description= data["weather"][0]["description"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.desctiption_label.setText(weather_description.capitalize())

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:      # Thunderstorm
            return "⛈️"

        elif 300 <= weather_id <= 321:    # Drizzle
            return "🌦️"

        elif 500 <= weather_id <= 531:    # Rain
            return "🌧️"

        elif 600 <= weather_id <= 622:    # Snow
            return "❄️"

        elif 701 <= weather_id <= 781:    # Atmosphere
            match weather_id:
                case 701:  # Mist
                    return "🌫️"
                case 711:  # Smoke
                    return "💨"
                case 721:  # Haze
                    return "🌁"
                case 731:  # Dust
                    return "🌪️"
                case 741:  # Fog
                    return "🌫️"
                case 751:  # Sand
                    return "🏜️"
                case 761:  # Dust
                    return "🌪️"
                case 762:  # Ash
                    return "🌋"
                case 771:  # Squall
                    return "💨"
                case 781:  # Tornado
                    return "🌪️"

        elif weather_id == 800:           # Clear
            return "☀️"

        elif weather_id == 801:           # Few clouds
            return "🌤️"

        elif weather_id == 802:           # Scattered clouds
            return "⛅"

        elif weather_id == 803:           # Broken clouds
            return "🌥️"

        elif weather_id == 804:           # Overcast clouds
            return "☁️"

        else:
            return "❓" 


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.setWindowTitle("Weather App")
    weather_app.show()
    sys.exit(app.exec_())