from json import load
from sys import path
import plotly.express as px
import plotly
import csv
import pathlib
import pandas as pd

from parseConfig import loadConfig

config = loadConfig()

p = pathlib.Path(config['dataRecordingSettings']['outputFolder'])

df = pd.DataFrame(dict(x=[], y=[]))

for f in p.iterdir():

    if f.suffix == '.csv':
        with open(f) as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            for row in csvReader:
                print(row)

    print()


# # df = px.data.gapminder().query("country=='Canada'")
# # fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

fig = px.line(df, x="x", y="y", title="Unsorted Input")

for _ in range(2):
    outputFolderPath = pathlib.Path(config['dataPlot']['outputFolder'])
    try:
        plotly.io.write_html(fig, outputFolderPath.joinpath('plot.html'))
    except FileNotFoundError:
        outputFolderPath.mkdir()
    else:
        break
# fig.show()
