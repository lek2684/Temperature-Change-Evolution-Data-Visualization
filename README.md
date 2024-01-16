READ ME
Project by Emily Kessel

For this project I was interested in looking at and visualizing the data supporting global warming. 
I used a data set (provided in canvas) acquired from https://data.giss.nasa.gov/gistemp/ 

Here’s what NASA says in reference to the GISTEMP data sets:
“The GISS Surface Temperature Analysis version 4 (GISTEMP v4) is an estimate of global surface temperature change…The basic GISS temperature analysis scheme was defined in the late 1970s by James Hansen when a method of estimating global temperature change was needed for comparison with one-dimensional global climate models.”
I used a data set that records the monthly average temperature deviations from the corresponding 1951-1980 averages. This data set ranges from the year 1880 to 2022.


CLEANING
The data set was well formatted and did not need a lot of cleaning. There were a few places where values were missing, and so I used a to_float function to address these and give them a default value.

PROCESSING
To process my data, I built a list of dictionaries, where my code would take a line of the source CSV file as a list and return a dictionary where the keys are column names and the values were the data. The dictionary keys correspond to the months (columns in the data set). After this, I aggregated the temperature changes by year, having my code average the temperature deviation for each year.

VISUALIZATION
I created a bar gar to visualize the temperature change trends over the course of the years 1880 to 2022. This visualization clearly shows, on average, global temperatures are rising.
