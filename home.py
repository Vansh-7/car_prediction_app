# Importing the necessary Python modules.
import streamlit as st
import numpy as np
import pandas as pd

# Configure the home as directed above.
def app():
  st.header("Car Price Prediction app")
  st.text(""" 
  This web app allows a user to predict the prices of a car based on their engine size, horse power, dimensions and the drive wheel type parameters.
  """)