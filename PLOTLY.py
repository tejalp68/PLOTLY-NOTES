# ----- New Cell -----
pip install plotly

# ----- New Cell -----
pip install --upgrade pip

# ----- New Cell -----
import plotly.express as px
import plotly.graph_objects as go

# ----- New Cell -----
## built in data set
df = px.data.iris()
df

# ----- New Cell -----
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="species")
fig.show()


# ----- New Cell -----
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 size="petal_length",color="species")
fig.show()


# ----- New Cell -----
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["sepal_width"],
    y=df["sepal_length"],
    mode="markers"
))

fig.show()


# ----- New Cell -----
fig = px.scatter_3d(df,
                    x="sepal_width",
                    y="sepal_length",
                    z="petal_length",
                    color="species")
fig.show()


# ----- New Cell -----
fig = px.line(df, x="sepal_width", y="sepal_length")
fig.show()


# ----- New Cell -----
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Scatter(x=df["sepal_width"],
                         y=df["sepal_length"]),
              row=1, col=1)

fig.add_trace(go.Bar(x=df["species"],
                     y=df["sepal_length"]),
              row=1, col=2)

fig.show()


# ----- New Cell -----
df_gap = px.data.gapminder()

fig = px.scatter(df_gap,
                 x="gdpPercap",
                 y="lifeExp",
                 animation_frame="year",
                 animation_group="country",
                 size="pop",
                 color="continent",
                 hover_name="country",
                 log_x=True)

fig.show()


# ----- New Cell -----
fig = px.bar(df, x="species", y="species_id")
fig.show()

# ----- New Cell -----
fig = px.bar(df, x="species", y="species_id",barmode ='group')
fig.show()

# ----- New Cell -----
x1,y1=[1,2,3,4,5,6] ,[5,2,3,6,7,4]
x2,y2=[1,2,3,4,5,6] ,[2,5,9,7,8,5]
x3,y3=[1,2,3,4,5,6] ,[4,8,6,5,1,2]

# ----- New Cell -----
fig =go.Figure()
fig.add_trace(go.Scatter(x=x1,y=y1))
fig.add_trace(go.Scatter(x=x2,y=y2))
fig.add_trace(go.Scatter(x=x2,y=y3))


# ----- New Cell -----
fig =go.Figure()
fig.add_trace(go.Scatter(x=x1,y=y1,name ="line1",mode="lines"))
fig.add_trace(go.Scatter(x=x2,y=y2,name ='Line2',mode ='markers'))
fig.add_trace(go.Scatter(x=x2,y=y3,name ='Line3',mode ='lines +markers'))


# ----- New Cell -----
color=['A','B','C','D','E','F']
fig=px.scatter(x=x1,y=y1,size=y1,color=color)
fig.show()

# ----- New Cell -----
x=[12,3,4,8]
y=[4,6,8,10]

# ----- New Cell -----
fig = go.Figure(go.Scatter(x=x,y=y,mode='markers'))
fig.show()

# ----- New Cell -----
fig = go.Figure(go.Scatter(x=x,y=y,mode='markers',marker_size=[90,60,70,80]))
fig.show()

# ----- New Cell -----


# ----- New Cell -----


# ----- New Cell -----


