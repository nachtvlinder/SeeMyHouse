# placeholder

import plotly.graph_objects as go
import pandas as pd
import rasterio

# Global variables
path = f""

# This will import the given file
# A filepath needs to be provided
# (pending feature) the coordinates
# available for plotting in 3D will
# be communicated to the user
# The user can then input a set
# of coordinates provided in WGS84,
# which is the standard most people know
print("Welcome to SeeMyHouse"
      "Unfortunately we don't have the functionality"
      "yet to build in the required data or "
      "fetch it from one of our servers ")
tiff_available = input("Can you provide your own GeoTIFF file for 3D plotting? (y/n)")
if tiff_available=="y":
    path = input("Please provide the filepath of your GeoTIFF: ")
    print(f"Your filpath: {path}")
else
    print("I'm afraid we can't help you yet, please contact"
          "mailto:maja.minnaert@gmail.com for further information")

# The next step is reading and windowing the given tiff file.
print("Examining file")
# Here comes the read statement,
# if possible providing exception
# message print-out for having
# the wrong file format and prompting
# retry with a suitable file
#codecomeshere

# Now that the file is confirmed we can ask for the coordinates
#codecomeshere

# and use them to read a window around the coordinates
#codecomeshere (rasterio window)

# followed by converting the resulting window,
# which is returned by rasterio as an nd-array,
# into a pandas dataframe
#codecomeshere

# We then use plotly to render a 3D plot
# of this dataframe, based on its x, y and z data.
#codecomeshere

# The following code is part of the first trial plot
# in the next steps, and will be tweaked to read in the
# converted numpy nd-array
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

# The following code already creates a trial plot
# in an automatically opened html file,
# and will be used to plot the data from the
# dataframe generated in the previous step
fig = go.Figure(data=[go.Surface(z=z_data.values)])

# The figure created in the previous step can be tweaked
# on its appearance/layout here. For personal note, the
# only thing I intend to change here is the colorscale.
# Todo: find a way to select a better colorscale
fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90),
                 colorscale=go.layout.Colorscale(diverging='greens'))

# This will save the plot
# to an interactive html file
# and open it in the standard browser
fig.write_html('HTML_plots/script_figure.html', auto_open=True)
