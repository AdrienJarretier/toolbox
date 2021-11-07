import plotly.graph_objects as go
import plotly
import csv
import pathlib
from datetime import datetime, timezone, timedelta
from averageToNPoints import averageToNPoints

from parseConfig import loadConfig

config = loadConfig()

p = pathlib.Path(config['dataRecordingSettings']['outputFolder'])

x = []
y = []
y2 = []


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
            if len(lines) > 0:
                header = lines[0]
                for i in range(1, len(lines)):
                    x.append(int(lines[i][0]))
                    y.append(toFloat(lines, i, 1))
                    y2.append(toFloat(lines, i, 2))

avgLen = 1669

x = averageToNPoints(x, avgLen)
y = averageToNPoints(y, avgLen)
y2 = averageToNPoints(y2, avgLen)


for i in range(len(x)):
    x[i] = datetime.fromtimestamp(
        x[i], timezone(timedelta(hours=0))).isoformat()

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y2,
                         mode='lines',
                         name='Sirsanga',
                         stackgroup='one'
                         ))

fig.add_trace(go.Scatter(x=x, y=y,
                         mode='lines',
                         name='Takama',
                         stackgroup='one'
                         ))


for _ in range(2):
    outputFolderPath = pathlib.Path(config['dataPlot']['outputFolder'])
    try:
        plotly.io.write_html(fig, outputFolderPath.joinpath('index.html'))
    except FileNotFoundError:
        outputFolderPath.mkdir()
    else:
        break

print('plot ready')
