'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
#okay so the x axis is the date so i need to obtain the first column of data, and then use that
#the y axis is the air quality, so i then need to go through the next 4 columns
#i add them togethetr and assign to a variable called air cleanliness or someting
#then i use atpltllib to make the graph
#simple easy calm

import matplotlib.pyplot as plt
import csv

with open('week-8-worksheet-main/t2-graph/leeds-centre-air-quality.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  

    dates = []
    avg_pollution = []

    for row in reader:
        try:
            date = row[0]
            pm25 = float(row[1])
            pm10 = float(row[2])
            o3 = float(row[3])
            no2 = float(row[4])

            average = (pm25 + pm10 + o3 + no2) / 4

            dates.append(date)
            avg_pollution.append(average)
        except ValueError:
            continue 


plt.plot(dates, avg_pollution)
plt.xlabel('Date')
plt.ylabel('Average Pollution')
plt.title('Ismael Charly Diarrassouba: Air Quality in Leeds Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("week-8-worksheet-main/t2-graph/plot.png")
plt.show()



