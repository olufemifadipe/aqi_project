# Air Quality Index (AQI) API Project

## Project Overview

This project is a Python-based application that retrieves real-time air quality and weather information using the IQAir AirVisual API. The application processes JSON data to provide information about local air quality conditions, including temperature, humidity, and Air Quality Index (AQI) readings.

Additionally, the application uses Folium to generate an interactive map displaying the geographical location of the air quality monitoring station.

This project was developed as part of my Component-Based Software Development coursework at Florida International University (FIU), with a focus on API integration, Python programming, JSON data handling, and data visualization.

## Key Features

- **Air Quality Monitoring:** Retrieves current air quality information using the IQAir API.
- **Weather Information:** Displays temperature in Celsius and Fahrenheit, along with humidity levels.
- **AQI Classification:** Categorizes air quality as good, moderate, unhealthy for sensitive groups, unhealthy, very unhealthy, or hazardous.
- **Interactive Mapping:** Uses Folium to create an HTML map showing the location associated with the air quality data.
- **JSON Processing:** Reads and writes JSON files using Python dictionaries and reusable functions.
- **API Authentication:** Loads the API key from a separate JSON configuration file.

## Technologies Used

- **Python 3** – Application development and data processing
- **IQAir AirVisual API** – Air quality and weather information
- **Requests** – HTTP requests and API integration
- **JSON** – Structured data storage and retrieval
- **Folium** – Interactive map generation
- **Git & GitHub** – Version control and project management

## Project Structure

```text
aqi_project/
├── aqi.py              # Main Python application
├── main_functions.py   # JSON file handling functions
├── aqi.json            # Retrieved air quality data
├── map.html            # Generated interactive map
├── .gitignore          # Excluded files and directories
└── README.md           # Project documentation
```

The `api_key.json` file is kept locally and excluded from GitHub to protect API credentials.

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/olufemifadipe/aqi_project.git
cd aqi_project
```

**2. Install the required Python packages**

```bash
pip install requests folium
```

**3. Configure your API key**

Create a file named `api_key.json` in the project folder and add:

```json
{
    "aqi_api_key": "YOUR_API_KEY_HERE"
}
```

Replace the placeholder with your own API key obtained from IQAir.

**4. Run the application**

```bash
python aqi.py
```

The application retrieves air quality information, saves the response to `aqi.json`, generates `map.html`, and displays the weather and AQI classification in the terminal.

## Example Output

The following example was generated using air quality data retrieved for George Town, Cayman Islands.

```text
The temperature is 29°C or 84.2°F,
the humidity is 78%, and the index shows
that the air quality is good.
```

The output changes based on the measurements returned by the API.

## Learning Outcomes

Through developing this project, I gained practical experience in:

- Integrating external REST APIs into Python applications.
- Understanding and processing JSON responses.
- Accessing nested dictionaries and lists.
- Implementing conditional statements for data classification.
- Creating reusable functions to organize application logic.
- Converting geographical coordinates into interactive visualizations.
- Managing source code using Git and GitHub.

## Future Improvements

Potential improvements include developing a graphical user interface, incorporating historical AQI trends, supporting searches by city, and creating visualizations that compare air quality conditions across different locations.

## Author

**Olufemi Rafael Fadipe**

B.S. Information Technology  
Florida International University (FIU)

*Developed for educational purposes as part of Component-Based Software Development coursework.*
