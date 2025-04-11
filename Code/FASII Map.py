# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 04:13:18 2025

@author: Natasha Pickard
"""


import folium

# Define site names, coordinates (longitude, latitude), and image URLs (verified public sources)
flood_mitigation_sites = {
    "FAS Phase 1 (City Centre)": {
        "coords": (-1.5470, 53.7946),
        "image": "https://www.arup.com/globalassets/images/projects/l/leeds-flood-alleviation-scheme/leeds-flood-alleviation-scheme.jpg"
    },
    "FAS Phase 2 Storage - Rodley": {
        "coords": (-1.6612, 53.8270),
        "image": "https://thefloodhub.co.uk/wp-content/uploads/2018/10/Landowner-offline-storage-2.png"
    },
    "Apperley Bridge Walls": {
        "coords": (-1.7120, 53.8380),
        "image": "https://www.yorkshireeveningpost.co.uk/webimg/b25lY21zOmQ3MDViYmMxLWUzM2MtNDhlMi1hYjE3LWU3N2I0ZjYzNzEwZTplMDFmZmIwMi03YTU1LTQwMzMtYTRkZC1jMGRkODYyOTRlZDc=.jpg?crop=3:2&trim=&width=800"
    },
    "Calverley Floodplain": {
        "coords": (-1.6840, 53.8370),
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Calverley_Woods_-_geograph.org.uk_-_1068994.jpg/640px-Calverley_Woods_-_geograph.org.uk_-_1068994.jpg"
    },
    "Moveable Weirs (Crown Point & Knostrop)": {
        "coords": (-1.5290, 53.7910),
        "image": "https://cdn.prgloo.com/media/bdf177e4da034def8dca06c48a11e15f.jpg?width=830&height=1245"
    },
    "Kirkstall Flood Walls": {
        "coords": (-1.5860, 53.8100),
        "image": "https://westleedsdispatch.com/wp-content/uploads/2023/06/leeds-flood-defence-works-Kirkstall-Bridge-900x675.jpeg"
    },
    "Woodland NFM (Upper Aire)": {
        "coords": (-2.0000, 53.9500),
        "image": "https://upperaire.org.uk/wp-content/uploads/2021/06/challenge-2.jpg"
    },
    "Riverbank Restoration (Kirkstall Goit)": {
        "coords": (-1.5760, 53.8115),
        "image": "https://westleedsdispatch.com/wp-content/uploads/2021/10/rsz_goit_image.jpg"
    }
}

# Create map centered over Leeds
m = folium.Map(location=[53.8008, -1.5486], zoom_start=12, tiles='OpenStreetMap')

# Add markers with image popups
for site, data in flood_mitigation_sites.items():
    lat, lon = data["coords"][1], data["coords"][0]
    image_url = data["image"]
    html = f"""
    <h4>{site}</h4>
    <img src="{image_url}" width="300">
    """
    iframe = folium.IFrame(html=html, width=320, height=250)
    popup = folium.Popup(iframe, max_width=320)
    folium.Marker(
        location=[lat, lon],
        popup=popup,
        tooltip=site,
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Save to HTML file
output_path = "leeds_flood_map_with_images.html"
m.save(output_path)
print(f"Map saved successfully to: {output_path}")
