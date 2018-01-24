from ipywidgets.embed import embed_minimal_html
import gmaps
from requests import get
import json
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
stations = get(url).json()['items']
gmaps.configure(api_key="PUT_YOUR_API_KEY_HERE")
ws_locations = [(station['weather_stn_lat'],station['weather_stn_long']) for station in stations]
info_box_template = """
<dl>
<dt>Station ID</dt><dd>{weather_stn_id}</dd>
<dt>Name</dt><dd>{weather_stn_name}</dd>
</dl>
"""
ws_info = [info_box_template.format(**station) for station in stations]
marker_layer = gmaps.marker_layer(ws_locations, info_box_content=ws_info)
fig = gmaps.figure(zoom_level=2,center=(25,0))
fig.add_layer(marker_layer)
embed_minimal_html('stations.html', views=[fig])
fig
