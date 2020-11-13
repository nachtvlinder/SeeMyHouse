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
