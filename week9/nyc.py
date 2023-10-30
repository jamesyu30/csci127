#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 29, 2023

import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)
mapCUNY.save(outfile='nycMap.html')