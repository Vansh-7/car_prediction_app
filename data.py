# Import necessary modules
import numpy as np  
import pandas as pd
import streamlit as st

# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(car_df)
    
    # Display descriptive statistics.
    st.subheader("Column Description:")
    if st.checkbox("Show summary"):
      st.table(car_df.describe())

    # Divide the web page into three columns to add more widgets.  
    beta_col1, beta_col2, beta_col3 = st.beta_columns(3)
    with beta_col1:
      if st.checkbox("Show all column names"):
        st.table(list(car_df.columns))
    
    with beta_col2:
      if st.checkbox("View Column Datatype"):
        st.table(list(car_df.dtypes))

    with beat_col3:
      if st.checkbox("View Column Data"):
        column_data = st.selectbox('Select column', tuple(car_df.columns)) 
        st.write(car_df[column_data])