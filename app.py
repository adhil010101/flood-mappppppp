from flask import Flask, render_template
import folium
import random

app = Flask(__name__)

# Simulated flood-prone locations within ~15 km radius of Ernakulam centre
flood_data = [
    {'name': 'MG Road', 'lat': 9.9816, 'lon': 76.2858, 'flood_level': random.randint(1, 10)},
    {'name': 'Kaloor', 'lat': 9.9987, 'lon': 76.2997, 'flood_level': random.randint(1, 10)},
    {'name': 'Edappally', 'lat': 10.0272, 'lon': 76.3089, 'flood_level': random.randint(1, 10)},
    {'name': 'Vyttila', 'lat': 9.9676, 'lon': 76.3182, 'flood_level': random.randint(1, 10)},
    {'name': 'Fort Kochi', 'lat': 9.9667, 'lon': 76.2425, 'flood_level': random.randint(1, 10)}
]

@app.route('/')
def index():
    # Center map on Ernakulam
    m = folium.Map(location=[9.9816, 76.2858], zoom_start=13)

    # Plot each location
    for location in flood_data:
        if location['flood_level'] >= 5:
            color = 'red'  # High flood risk
        else:
            color = 'green'  # Low flood risk

        folium.Marker(
            location=[location['lat'], location['lon']],
            popup=f"{location['name']} - Flood Level: {location['flood_level']}",
            icon=folium.Icon(color=color)
        ).add_to(m)

    # Save map as HTML file
    m.save('templates/map.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
