
# Weather App

This is a Python web application built with Flask that allows users to check the weather of a city using the OpenWeatherMap API.

## Prerequisites

Before running the application, make sure you have the following prerequisites:

- Python 3.x installed
- Flask framework installed ( `pip install flask` )
- Requests library installed ( `pip install requests` )

## Getting Started

1. Clone the repository:
    - git clone https://github.com/adriannavarrobetrian/ikigai.git
    - cd python/weatherapp

2. Set up the API key:

   - Sign up for an account at [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
   - Create a file named  `.env`  in the project root directory.
   - Add the API_KEY=<your-api-key>  to the  `.env`  file.

3. Run the application:

   - python app.py

4. Open your web browser and navigate to  `http://localhost:8000`  to access the Weather App.

## Usage

- Enter the name of a city in the input field and click the "Get Weather" button.
- The application will retrieve the weather information for the specified city from the OpenWeatherMap API and display it on the page.

## License

This project is licensed under the [MIT License](LICENSE).

