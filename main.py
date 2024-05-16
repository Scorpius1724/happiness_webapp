import streamlit as st
import pandas as pd
import plotly.express as px

def data_selection(X_axis, Y_axis):
    match X_axis:
        case "Happiness":
            X_data = Happiness
        case "GDP":
            X_data = GDP
        case "Social support":
            X_data = Social_support
        case "Generosity":
            X_data = Generosity
        case "Corruption":
            X_data = Corruption
    match Y_axis:
        case "Happiness":
            Y_data = Happiness
        case "GDP":
            Y_data = GDP
        case "Social support":
            Y_data = Social_support
        case "Generosity":
            Y_data = Generosity
        case "Corruption":
            Y_data = Corruption
    return X_data, Y_data

df = pd.read_csv("happy.csv")

Happiness = df["happiness"].to_list()
GDP = df["gdp"].to_list()
Social_support = df["social_support"].to_list()
Generosity = df["generosity"].to_list()
Corruption = df["corruption"].to_list()

st.title("In Search for Happiness")

X_axis = st.selectbox("Select the data for the X-axis",
                      ("Happiness", "GDP", "Social support", "Generosity", "Corruption"))
Y_axis = st.selectbox("Select the data for the Y-axis",
                      ("Happiness", "GDP", "Social support", "Generosity", "Corruption"))

st.subheader(f"{X_axis} and {Y_axis}")

X_data, Y_data = data_selection(X_axis, Y_axis)

figure = px.scatter(x=X_data, y=Y_data, labels={"x": X_axis, "y": Y_axis})
st.plotly_chart(figure)