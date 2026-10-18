import main_functions
import requests
import folium
#TODO return your api key as a string

"""task6"""
def get_api_key(filename):
    data = main_functions.read_from_file(filename)
    return data['aqi_api_key']


my_aqi_api_key = get_api_key('api_key.json')
print(my_aqi_api_key)

"""task7"""
def get_aqi_data(api_key):
    url = "http://api.airvisual.com/v2/nearest_city?key="
    url_aqi = url + api_key

    response = requests.get(url_aqi)
    data = response.json()
    main_functions.save_to_file(data,"aqi.json")

get_aqi_data(my_aqi_api_key)

    # TODO: Make the API request and save the result into a JSON file

"""task8"""
def generate_map(data_filename,zoom_start):
    aqi_data = main_functions.read_from_file(data_filename)

    lat = aqi_data['data']['location']['coordinates'][1]
    long = aqi_data['data']['location']['coordinates'][0]

    m = folium.Map(location=[lat, long], zoom_start=zoom_start)
    folium.Marker(
        location=[lat, long],
        popup='AQI Station',
        icon=folium.Icon()
    ).add_to(m)
    m.save("map.html")

generate_map("aqi.json", 10)

"""task9"""
def display_aqi_info(data_filename):
    aqi_data = main_functions.read_from_file(data_filename)
    tempC = aqi_data['data']['current']['weather']['tp']
    tempF = (tempC * 9 / 5) + 32
    humid = aqi_data['data']['current']['weather']['hu']
    aqius = aqi_data['data']['current']['pollution']['aqius']

    if aqius <= 50:
        quality ="good"
    elif aqius <= 100:
        quality ="moderate"
    elif aqius <= 150:
        quality ="unhealthy for sensitive groups"
    elif aqius <= 200:
        quality ="unhealthy"
    elif aqius <= 300:
        quality ="very unhealthy"
    else:
        quality = "hazardous"

    print(f"The temperature is {tempC}°C or {tempF:.1f}°F, "f"the humidity is {humid}%, and the index shows "f"that the air quality is {quality}.")

display_aqi_info("aqi.json")
    # TODO: print the message shown above with the values assigned above. Notice that tempF needs to be calculated!