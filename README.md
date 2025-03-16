Weather App - Python


A lightweight desktop application built with Python to fetch and display real-time weather information for any city using the OpenWeatherMap API. The app features a simple graphical user interface (GUI) created with Tkinter, allowing users to input a city name and view details like temperature, weather description, humidity, and wind speed.
Features
Input a city name to retrieve current weather data.
Displays weather details: temperature (°C), description, humidity (%), and wind speed (m/s).
User-friendly GUI with error handling for invalid inputs or API issues.
Responsive design with organized layout.
Components and Libraries Used
Tkinter  
Python’s standard GUI toolkit used to build the app’s interface.  
Components:  
Tk: Main application window titled "Weather App".  
Frame: Organizes input and output sections with padding for better layout.  
Label: Displays static text (e.g., "City:") and dynamic weather results.  
Entry: Text field for users to input the city name.  
Button: "Get Weather" button to trigger the weather fetch.  
messagebox: Pop-up warnings for input errors (e.g., empty city field).
Requests  
HTTP library used to make GET requests to the OpenWeatherMap API.  
Handles API communication and retrieves weather data in JSON format.
JSON (built-in, via requests)  
Parses the JSON response from the API into a Python dictionary for easy data extraction.
OpenWeatherMap API  
External weather service providing real-time data.  
Endpoint: http://api.openweathermap.org/data/2.5/weather.  
Parameters: City name (q), API key (appid), and metric units (units=metric).  
Returns temperature, weather description, humidity, and wind speed.
Exception Handling  
Uses try/except to manage:  
requests.exceptions.RequestException: Network or API errors.  
KeyError: Invalid API response data.
Provides user-friendly error messages in the GUI.
How It Works
The app launches a Tkinter window with an input field for the city name and a "Get Weather" button.
Upon clicking the button, the fetch_weather() function retrieves the city input and calls get_weather() with the API key and city name.
The API response is processed, and weather details are displayed in a formatted string on the result_label.
If the city is invalid or an error occurs, an error message is shown instead (e.g., via messagebox for empty input).
Prerequisites
Python 3.x installed.
Install required library:  
bash
pip install requests
A valid OpenWeatherMap API key (currently hardcoded as 4fe89575303fffeeb70f036298389f59 in the code).
Usage
Clone the repository:  
bash
git clone <repository-url>
Replace the API key in the code with your own OpenWeatherMap API key (or store it securely, e.g., in an .env file).  
Run the app:  
bash
python weather_app.py
Enter a city name (e.g., "London") and click "Get Weather" to view the results.
Code Structure
get_weather(api_key, city): Fetches weather data from the API and returns a dictionary or error message.
fetch_weather(): Handles GUI interaction, validates input, and updates the display.
GUI Setup: Configures the Tkinter window with input and output frames.
Future Improvements
Store the API key in an environment variable for security.
Add support for additional weather metrics (e.g., pressure, sunrise/sunset).
Include a history of searched cities or a dropdown for recent searches.
Enhance the UI with colors, icons, or a background theme.
