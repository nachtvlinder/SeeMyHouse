# SeeMyHouse
An application that shows a 3D model of the building/house at a given location based on coordinates.

## About

### What
A backend and interface for rendering a 3D model of a house at given 
coordinates in the area of Bruges, Belgium.

Extras, pending further inspiration, will be listed here.

### Why
Imagine a world where everyone can see their house, not by just walking outside and
looking at it, but by looking up the coordinates and typing them into some webpage or app
that then shows them a 3D model of their house based on LIDAR data. Wouldn't that be
awesome?

Also I want to show you what I can do with a keyboard, an internet connection and a decent
computer.

### When
Started: November 6, 2020

Deadline: November 20, 2020

### How
Challenges arose in the windowing mainly, during the whole of the first week.
The evolution and general approach will
be described here as time passes. A first glance of
this, including issues encountered and
solutions/approaches found and tested, 
is available in the November 10 section of the
[workflow](workflow.md) file, and will be 
integrated in this README.md section early next working day.

Also see the daily [workflow](workflow.md) report. 

#### Approach and vague planning
The current phase is one of exploration: of the data, the files, needed libraries. It
is also a time of new beginnings: of the github repository, the notebook and other files in it, 
this readme file and an integrated PyCharm-centered workflow.

The future brings: extended data reconnaissance and iteratively building up the
required plots. ETA for finishing improvable basic prototype visualizations: tuesday-ish.

### Who
Maja Minnaert for BeCode

## Project To-Do List
There's also a [daily](daily.md) checklist.

### Pending
- [x] Archive research files
- [ ] Clean up py-script code and comments
- [ ] Clean up and fill this README's first sections
- [ ] Do some final testing
- [x] Reverse x axis to prevent mirrored plot

### Extra tweaks (optional) 
*(dash and gui's only in branch 'dash-deployment'!!!)*
- [x] Set up Github Page
- [ ] Study dash app implementation
- [ ] Design: make prototype interface
- [ ] Deploy and test dash app
- [ ] Set up project Github Page for information/presentation
- [ ] Make zip file with the script and a short readme with 
instructions for use
- [ ] Make that zip available on the project website
- [ ] Link to dash app on the project website

### Done
- [x] Set up environment in pycharm
- [X] Install needed base packages
- [x] Set up project repository
- [x] Link pycharm project to github repository
- [x] Pimp up the readme file
- [x] Set up md file "workflow.md" for daily reporting
- [x] Check what geopandas is
- [x] Install geopandas
- [x] Determine use case data subset
- [x] Download the data
- [x] Add notebook for example files & gpd learning
- [x] Add [notes](Archive/notes.txt) file for virtual post-its
- [x] Explore Data: study file types
- [x] Learn to work with geopandas
- [x] Explore Data: look at data contents
- [x] Explore Data: determine, try-out and find/choose needed packages
- [x] Switched to plotly
- [x] Made basic first figure with plotly
- [x] Find out how to 3D plot AOI
- [x] Design: check for interface requirements?
- [x] Updated [notes](Archive/notes.txt) with approach tips from debrief
- [x] Created first script file [SeeMyHouse-CLI](SeeMyHouse-CLI.py)
- [x] Added comments in CLI-script to describe the algorithm
 in human language
- [x] Translate script comments into code for interpreter
- [x] Write text interface (input and print statements)
- [x] Read geotiff into rasterio object
- [x] Convert coordinates
- [x] Construct window --> Complication raised
- [x] Convert window from nd-array to pandas dataframe --> Complication risk
- [x] Tie dataframe into plotly code --> Should be fairly straightforward
- [x] Fix scaling/spiking issue responsively