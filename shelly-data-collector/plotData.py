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


def toFloat(val):
    try:
        if val != '':
            return float(val)
        else:
            return 0.0
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
            for row in lines[1:]:
                x.append(datetime.fromtimestamp(int(row[0])).isoformat())
                y.append(toFloat(row[1]))
                y2.append(toFloat(row[2]))


# df = px.data.gapminder().query("country=='Canada'")
# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

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
