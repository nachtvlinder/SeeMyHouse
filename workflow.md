# Daily workflow reports
## November 6, 2020
Set up git repository and project page,
filled in details on the readme file and 
studied the data files, their file types, the geopandas
library and started up a notebook for initial
data reconnaissance.
## November 9, 2020
Explored the data and imported a subset into my 
pycharm project folder. 
First code tryouts in jupyter notebook revealed what
other libraries are useful/needed. Ran into issue
when pygeos was installed, eventually removed this
and reïnstalled geopandas to resolve the issue it
caused in geopandas.

The Jupyter Notebook workflow is up and running now,
Still researching ways to plot in 3D and to read the
relevant data from the available files. I certainly
have a clearer view of what needs to be done in terms
of visualization code. The data types are still unclear,
but exploring them through jupyter notebook and the 
libraries and as such learning by doing looks promising.

Basically, I'm in the middle of exploring the multitude
of approaches findable out there, and starting to get
some overview and idea of what direction to go
to zoom in on the most efficient methods.
## November 10, 2020
Trying to plot tif files and shapefiles, learning
to make sense of them and how they can
be used for the project at hand. Found some
hands on learning materials, discovered plenty
libraries that can be used.

I thought: if GeoTIFF is an image format, there
should be an image-viewer out there who can view
it. That's how I ended up downloading QGIS, which
offers this functionality and more, and the 
QGIS website offers great material on learning
to work with geospatial data and GIS data.
I would recommend their training manual and/or their
gentle introduction to GIS to others facing
the same challenge and not familiar with the GIS
data and filetypes we encounter here. (Links TBA)

I researched on and experimented with rasterio, gdal
and QGIS, ending up with a lot more insight in the
data and how to apply it to this use case. Now
I'm in the process of familiarizing myself with the
programming techniques and methods that I need
for implementing a solution in python. I considered
using the QGIS API for standalone python applications,
but resorted to going with the python approach. The latter
is supported by a very applicable Datacamp course. I filed
the notion of QGIS existence for further personal learning,
since GIS scores high as a field of interest for me.
Another advantage to familiarizing myself with QGIS was
the ability to explore the data without waiting for the
comparably slow runtimes of my jupyter notebook and python
code. QGIS is implemented in C++, which explains the
difference in GPU/CPU demands on my local system. QGIS
is needed to overcome the limitations of my local technology,
and will help me gain the insight to implement the python
solution in fewer trial runs on my local jupyter notebook kernel.
(these notes to be integrated in README.md's How-section)

Practical takeaways from today: using the shapefile to select
a portion of the GeoTIFF containing the needed elevation
data, as seen an example of in QGIS tutorials. This makes me
confident that QGIS will be of key assistance in understanding the
other materials, and can be used as a sort of pseudo-coding
learning experience before learning and attempting to implement
the same functionality in my own python application. On the other
hand I frequently attempt new steps in that process by implementing
newly learned steps and insights in a jupyter notebook, and by finding
online how to take the next step.

Planning to learn this, meanwhile also learning through the
Datacamp resource and a book on using QGIS on Packt (links TBA).
It's worthwhile to note attention goes to prioritizing the
python/gdal/rasterio workflow and the direct results for the
challenge project over extra learning about
GIS, QGIS and the ways this and python can work together.
That said, it's exciting to learn in this direction, and to
discover them through developing for this project.

Next steps:
- How to slice the shapefile? Learning to use geopandas for this.
- What are the other files in the zip for? Might google these as aside.
- Overlaying the tif with the shapefile to select the needed area to plot.
- From there, 3D plotting the resulting slice will be the next challenge.
QGIS looks helpful for determining the substeps of this 3D modeling process,
before finding the python-based implementation step by step.
## November 12, 2020

### Done today:
- Determined dataset boundary
 for development use to one geotiff file
- Figured out coordinate systems and CRS conversion

### Still trying or partially succeeded:
- Getting the precise needed conversion 
 EPSG codes for the data at hand
- Zooming in on a section of the DSM based on a
coordinate point
- 3D plotting from a (section of a) geotiff file

### How it went:
At first I jumped a bit back and forth between using the shapefile
and the geotiff file, where I learned more about the
difference and determined the data needed for this
application is in the geotiff file. I used QGIS to 
explore the data to select the most useful geotiff file.

QGIS visualization (with the program) helped with
fast looking in sufficient detail at the .tif files, by
cutting out loading times.
After finding the city area on one of these, I discarded
the other zipfile contents to focus on this
NGI map section since it contains the area that will
be used in verifying the solution.

I managed to collect information on the geotiff attributes
using the rasterio library. Plotting the file data
is still too slow, so focus should now be directed
to zooming in on a chosen bounding box, and to do so based
on coordinates within that bounding box (the former
and latter are separated on the todolist).

## November 13, 2020
Experimented further with crs conversion and windowing. Portion of the 
day went to work on presentation and some time was lost
with an internet technician's visit. This is, however,
partly good news since connection problems slowing down
the work should soon be a thing of the past here.

Not much code has changed or been added, mainly reading and 
insight building was done today. This does bring me closer to
realizing the goals of the project.

## November 16, 2020
Started in reverse today, trying to plot a 3D elevation model based
on the plotly getting started pages on their website. This worked, 
and I attempted to apply a custom colorscale to this as I had found
one through another code approach found online. The source of the latter
is found atop [the new plotly notebook](Archive/plotly.ipynb). The second approach listed
at the top with a source URL is partially implemented there. Next working day
I will move on to the more urgent matter of slicing, which has been a muddy
area last week. I presume external issues have impacted my workflow there.
*I'm still unsure how and with what tool I could manage to parse the GeoTIFF
into a dataframe or geodataframe that holds x, y and z values
for plotly to use and draw.* I would like to accomplish this tomorrow so 
I can implement some UX and interface ideas and tweak the end-results in the last two
days running up to the deadline.

The issue of parsing geotiff to dataframe was
brought up during debrief, resulting in getting
some very usable advice from a colleague. I notes this 
in my [notes](Archive/notes.txt) file, intending
to implement these into my project todolist.
Fingers crossed for getting this backend algorithm
figured out fast tomorrow.

In the evening, I prepared a py-file with 
the needed comments to describe the planned
algorithm, ready to be translated one by one
into python code. This is the main objective
for tomorrow, November 17: to get this as a functional
script with the desired outcome. Expansion can be
made later, including a simple GUI. I also updated
the project todolist accordingly.

## November 17, 2020
My workday was split, due to personal affairs,
into yesterday evening prep and code work today.

Yesterday evening I prepared a python script file
with the steps to encode (algorithm) in the form
of comments. I also explored a bit the options
of how to implement a simple GUI or a functional
web-app on the project Github Page, respectively using
PySimpleGUI and Brython. I'll also look into Dash.

However priority remains with implementing the
minimum requirements in a qualitative way. This
is what I spent today doing. More specifically,
I encoded the user input prompts and communication
towards the user for a text-based interface, making
it possible for the user to provide a filepath
and coordinates after asking questions about compatibility
with simple question-form input statements. In
tandem with this process the necessary data is read
into variable objects. Next I encoded the reading
into rasterio object of the GeoTIFF file, the request
of coordinates from the user, their conversion to Belgian
Lambert from WGS84, and the construction of border values
for the bounding box or window to be sliced from 
the rasterio object. 

At this point I ran into complications with
implementing the rasterio windowing method. This 
happened near the end of the workday, which puts 
it immediately on the planning for next working
session. I adopted a code line from our team
chat which I have yet to analyze in further detail
at that time.

## November 18, 2020
Today I implemented nearly all of the steps in the
basic python script, which will be maintained as
the product in its most basic form. Tomorrow I 
hope to both implement a simple GUI using PySimpleGUI
and Brython to make this available on the Github Page
linked to the project repository. 

Implemented today:
- Text interface
- Conversions of coordinates
- Selecting window around coordinate
- Repeated testing
- Testing different coordinates
- Analyzing spiking problem
- Finishing touches on plotting

Improvements in mind:
- Making the code somewhat more modular, so
it can be extended upon with different UX interfaces
- Deploying a simple GUI interface
- If possible deploying a web accessible interface
- Fixing the spiking/scaling problem

Overall this was a very productive day, thanks to the many
research and preparations done in previous days.
