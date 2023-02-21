from collections import namedtuple
import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px

# Load some sample data
data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 32, 18, 47, 29],
    'income': [50000, 70000, 30000, 90000, 60000],
    'gender': ['F', 'M', 'M', 'M', 'F'],
    'city': ['New York', 'San Francisco', 'New York', 'Boston', 'Chicago']
})

# Set page title and favicon
st.set_page_config(
    page_title="Streamlit Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add a title
st.title('My Streamlit Dashboard')

# Add a sidebar for filtering data
st.sidebar.subheader('Filter Data')
min_age, max_age = st.sidebar.slider('Select age range', 18, 60, (25, 50))
selected_cities = st.sidebar.multiselect('Select cities', data['city'].unique(), default=['New York'])

# Apply filters to data
filtered_data = data[(data['age'] >= min_age) & (data['age'] <= max_age) & (data['city'].isin(selected_cities))]

# Add a bar chart of income by gender
st.header('Income by Gender')
gender_income = filtered_data.groupby('gender')['income'].mean()
st.bar_chart(gender_income)

# Add a line chart of income by age
st.header('Income by Age')
age_income = filtered_data.groupby('age')['income'].mean()
fig = px.line(x=age_income.index, y=age_income.values, labels={'x': 'Age', 'y': 'Income'})
st.plotly_chart(fig)

# Add a table of the filtered data
st.header('Filtered Data')
st.write(filtered_data)

# Add responsiveness for different screen sizes
col1, col2 = st.beta_columns([2, 1])
with col1:
    st.write('This is in the left column')
with col2:
    st.write('This is in the right column')



"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:



with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
        
"""
