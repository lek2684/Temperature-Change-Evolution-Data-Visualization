#-------------------------------------------------------------------------
#Visualization of Earth's average temperature trends from 1880 to 2022

#
# NASA data
# https://data.giss.nasa.gov/gistemp/
#-------------------------------------------------------------------------
import csv
from tkinter import Tk, Canvas
#-------------------------------------------------------------------------
# Constants for visualization pixel values
#-------------------------------------------------------------------------
GUTTER = 30 # space around chart
CHART_WIDTH = 1500
CHART_HEIGHT = 350
CANVAS_WIDTH = CHART_WIDTH + GUTTER * 2
CANVAS_HEIGHT = CHART_HEIGHT + GUTTER * 2
BAR_COUNT = 170 
#-------------------------------------------------------------------------
# Convert strings to floats
#-------------------------------------------------------------------------
def to_float(value : int, default_value = 0.0):
   
    if value.strip() == '': return default_value # for non-numerical entry (places where the boxes are filled with ***)
    try:
        return float(value.strip())
    except:
        print('Bad float value:', value)
        return default_value
#-------------------------------------------------------------------------
# Functions to map data values to pixel dimensions
#-------------------------------------------------------------------------
def avgtemp_to_height(avgtemp: float):
    return (avgtemp)*CHART_HEIGHT

#-------------------------------------------------------------------------
# Functions to draw bars for the visualization
#-------------------------------------------------------------------------
def draw_avgtemp_bar(canvas, x, width, avgtemp):
    height = avgtemp_to_height(avgtemp)
    y = CHART_HEIGHT + GUTTER - height
    canvas.create_rectangle(x, y, x + width, y + height, fill = 'darkgreen')

#-------------------------------------------------------------------------
# take line of the source CSV file as a list and return a dictionary where the keys are column names and the values are the data
def load_data_row(row):
    
    year = float(row[0])
    January = to_float(row[1])
    Feburary = to_float(row[2])
    March = to_float(row[3])
    April = to_float(row[4])
    May = to_float(row[5])
    June = to_float(row[6])
    July= to_float(row[7])
    August = to_float(row[8])
    September = to_float(row[9])
    October = to_float(row[10])
    November = to_float(row[11])
    December = to_float(row[12])

    return {
    'Year': year,
    'January' : January,
    'Feburary' : Feburary,
    'March' : March,
    'April' : April,
    'May' : May,
    'June' : June,
    'July' : July,
    'August' : August,
    'September' : September,
    'October' : October,
    'November': November,
    'December': December
    }


#-------------------------------------------------------------------------
# Draw legend
#-------------------------------------------------------------------------
def draw_legend(canvas):
    canvas.create_rectangle(
    GUTTER + CHART_WIDTH - 500, GUTTER,
    GUTTER + CHART_WIDTH - 480, GUTTER + 20,
    fill = 'darkgreen')
    canvas.create_text(
    GUTTER + CHART_WIDTH - 470, GUTTER,
    text = 'Avg Yearly Global Change in Temp', anchor = 'nw')
   
def draw_data_bars(canvas, years):
    x = GUTTER
    count = 0
    bar_width = ((CHART_WIDTH) / BAR_COUNT) 

    for year in sorted(years.keys()):
        avgtemp = years[year]
        draw_avgtemp_bar(canvas, x, bar_width, avgtemp)
        x += bar_width

        # Draw year as text
        canvas.create_text(x, CHART_HEIGHT + GUTTER + 10, text=str(int(year)), fill="black", font='Helvetica 5')
        x+=1

        count += 1
        if count >= BAR_COUNT:
            break
#-------------------------------------------------------------------------
# Open data file and create list of data rows
#-------------------------------------------------------------------------

file = open('global-temps.csv')
next(file) # skip header rows
next(file)
next(file)
next(file)
next(file)
     
data_reader = csv.reader(file)
dataset = [ ]
for row in data_reader:
    fields = load_data_row(row)
    dataset.append(fields)
#-------------------------------------------------------------------------
# aggregate the temperature changes by year
#-------------------------------------------------------------------------
years = {}

# Iterate through the dataset
for values in dataset:
    year = values['Year']

    # find average global temperature change for the year
    avgtemp = (sum(values.values()) - year)/12  # Exclude the 'Year' value from the sum

    # Store the aggregated value in the years dictionary
    years[year] = avgtemp

#-------------------------------------------------------------------------
# Create Tkinter window
#-------------------------------------------------------------------------
gui = Tk()
gui.title('Average Yearly Global Temperature Increase from 1880 to 2022')
canvas = Canvas(gui, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
background='white')
canvas.pack()
canvas.create_rectangle(
GUTTER, GUTTER,
GUTTER + CHART_WIDTH, GUTTER + CHART_HEIGHT,
fill = 'white', outline = 'black')
#-------------------------------------------------------------------------
# Create visualization
#-------------------------------------------------------------------------

draw_data_bars(canvas, years)
draw_legend(canvas)
canvas.mainloop()
