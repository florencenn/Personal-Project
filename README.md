# MA705-Personal-Project-FlorenceGu
 MetMuseum

## Dashboard Description
------------
The Metropolitan Museum of Art presents over 5,000 years of art from around the world.
Founded in 1870, The Museum lives in two iconic sites in New York City, USA. 
The dashboard summarizes the information of over seven hundred objects information from MET.

This purpose project is designed to simulate the trend that how’s the new enroll collections’ amount changes during World War II Period.
Considering the effect after the war, this database also includes two more years after year 1945.

In this app, it has a drop-down menu and checkbox to choose either obeject's category or the year that the museum obtained it.
Providing administrators mutiple clicks access to most pages.  

 * For a full description of the module, visit the project page:
  https://metmuseumbyflorence.herokuapp.com



## REFERENCES:
------------
Here is a list of data sources and references used in this course project.
The Metropolitan Museum of Art Collection API:https://metmuseum.github.io
Dash Plotly Multipel Output & Input:https://www.youtube.com/watch?v=dgV3GGFMcTc&t=1758s
Interactive Dashboard with Python: https://www.youtube.com/watch?v=acFOhd



## Difficulty
------------
One of the problem I encounter is when I load all the codes in my locate computer, 
the dashboards work well. But when I upload it into the Heroku, all the layout showed up but 
not the data. I check the data file in heroku and it showed all the content. It took me hours 
to find why the heroku cannot read my dataframe, and appear empty dataframe. 
It's the pandas version in requirements file not the same as my local pandas version.
After changing the pandas version in the requirements file, the dashboard works.