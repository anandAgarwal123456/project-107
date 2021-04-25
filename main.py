import csv
import pandas as pd
import plotly.graph_objects as pg

df = pd.read_csv("project-107-data.csv")

studentDf = df.loc[ df['student_id'] == 'TRL_zet' ]
print(studentDf)
print(studentDf.groupby("level")["attempt"].mean())

fig = pg.Figure(pg.Bar(
    x = studentDf.groupby('level')['attempt'].mean(),
    y = ['Level 1', 'Level 2', 'Level 3' , 'Level 4'],
    orientation= 'h'
))

fig.show()