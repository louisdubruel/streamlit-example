import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

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
fig, ax = plt.subplots()
sns.barplot(x='gender', y='income', data=filtered_data, ax=ax)
st.pyplot(fig)

# Add a line chart of income by age
st.header('Income by Age')
fig, ax = plt.subplots()
sns.lineplot(x='age', y='income', data=filtered_data, ax=ax)
ax.set_xlabel('Age')
ax.set_ylabel('Income')
st.pyplot(fig)

# Add a table of the filtered data
st.header('Filtered Data')
st.write(filtered_data)

# Add responsiveness for different screen sizes
col1, col2 = st.beta_columns([2, 1])
with col1:
    st.write('This is in the left column')
with col2:
    st.write('This is in the right column')
