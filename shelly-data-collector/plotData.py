import plotly.graph_objects as go
import plotly
import csv
import pathlib
from datetime import datetime
import math

from parseConfig import loadConfig

config = loadConfig()

p = pathlib.Path(config['dataRecordingSettings']['outputFolder'])

x = []
y = []
y2 = []

# # returns a list of size n averaged data from originalData
# def averageToNPoints(originalData, n):



def toFloat(lines, i, j):
    val = lines[i][j]
    try:
        if val != '':
            return float(val)
        else:
            if i == 1:
                return toFloat(lines, i+1, j)
            elif i == len(lines)-1:
                return toFloat(lines, i-1, j)
            else:
                return (toFloat(lines, i-1, j)+toFloat(lines, i+1, j))/2
    except ValueError as ve:
        print(ve)
        print(val)


for f in p.iterdir():

    if f.suffix == '.csv':
        with open(f) as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            print(f)
            lines = list(csvReader)
            header = lines[0]
            for i in range(1, len(lines)):
                x.append(datetime.fromtimestamp(int(lines[i][0])).isoformat())
                y.append(toFloat(lines, i, 1))
                y2.append(toFloat(lines, i, 2))


# df = px.data.gapminder().query("country=='Canada'")
# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

# fig = go.Figure(layout=go.Layout(width=1920))
fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y,
                         mode='lines',
                         name=header[1],
                         stackgroup='one'
                         ))

fig.add_trace(go.Scatter(x=x, y=y2,
                         mode='lines',
                         name=header[2],
                         stackgroup='one'
                         ))


for _ in range(2):
    outputFolderPath = pathlib.Path(config['dataPlot']['outputFolder'])
    try:
        plotly.io.write_html(fig, outputFolderPath.joinpath('plot.html'))
    except FileNotFoundError:
        outputFolderPath.mkdir()
    else:
        break

print('plot ready')
