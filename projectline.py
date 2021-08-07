import pandas as pd
import plotly.express as px

df = pd.read_csv('project.csv')

fig = px.line(df,x='date',y='cases',color='country',title='Corono cases on different dates')
fig.show()