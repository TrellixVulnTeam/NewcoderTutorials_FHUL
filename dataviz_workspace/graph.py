"""
Data Visualization Project
Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.
Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

import parse
from parse import parse, MY_FILE
import parse as p


def visualise_days():
    """Visualise data by day of the week"""


    # grab previously parsed data
    data_file = p.parse(p.MY_FILE, ",")

    # create variable 'counter', counts each match for the string "Day of Week"
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate out the counter to order it correctly when plotting.
    data_list = [counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]
    # need a tuple for plt.xticks()
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # assign y-data to instance of a matplotlib plot
    plt.plot(data_list)

    # assign labels to the plot
    plt.xticks(range(len(data_list)), day_tuple)

    # save the plot!
    plt.savefig("Days.png")

    # close the figure
    plt.clf()


def visualise_type():
    """Visualise data by category in a bar graph"""

    # grab our parsed data
    data_file = parse(MY_FILE, ",")

    # make a new variable, 'counter', from iterating through each line
    # of data in the parsed data, and count how many incidents happen
    # by category
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter.
    # Since order doesn't matter, we can just used counter.keys()
    labels = tuple(counter.keys())

    # Set exactly where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar that will be plotted
    width = 0.5

    # Assign data to a bar plot (similar to plt.plot()!)
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give some more room so the x-axis labels aren't cut off in the
    # graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure is larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the graph!
    plt.savefig("Type.png")

    # Close plot figure
    plt.clf()



def main():
    # visualise_days()
    visualise_type()

if __name__ == "__main__":
    main()
