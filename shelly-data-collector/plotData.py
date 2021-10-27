from json import load
import plotly.express as px

from parseConfig import loadConfig

config = loadConfig()



df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
# fig.show()
