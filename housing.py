# Common Libraries used
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Shiyu Wei')
df = pd.read_csv('housing.csv')

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults top 3 countries in population

# filter by location
df1 = df[df.ocean_proximity.isin(location_filter)]

level_fliter = st.sidebar.radio(
    'choose income level',
    ('low','medium','high')
    )

if level_fliter == 'low':
    df2 = df1[df.median_income <= 2.5]
elif level_fliter == 'medium':
    df2 = df1[df.median_income <= 4.5]
    df2 = df1[df.median_income >= 2.5]
elif level_fliter == 'high':
    df2 = df1[df.median_income > 4.5]
    

price_filter = st.slider('Median House Price:', 0, 500001, 200000)  # min, max, default


# filter by price
df3 = df2[df2.median_house_value <= price_filter]

# show on map
st.map(df3)

# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots()
ax.hist(df3['median_house_value'], bins=30)
st.pyplot(fig)
