# import libraries
import streamlit as st
import plotly.express as px
import pandas as pd


# import dataset
df= px.data.gapminder()
st.header("Data set")
st.write(df)

st.text("Column names in data frame")
st.write(df.columns)

# summary stats
st.write(df.describe())

# data managment

year_option = df["year"].unique().tolist()

year = st.selectbox("which year should we plot",year_option,0)

# df= df[df["year"]==year]

# plotting
fig = px.scatter(df, x ="gdpPercap",y ="lifeExp",size="pop",color="country",hover_name="country",
                log_x=True,size_max=55,range_x=[100,100000],range_y=[20,90],
                animation_frame="year", animation_group="country")

fig.update_layout(width=800, height =600)
st.write(fig)