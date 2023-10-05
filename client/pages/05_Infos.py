import requests
import pandas as pd
import streamlit as st


# Create a dropdown menu to select the country
response = requests.get(f"http://127.0.0.1:8000/unique_countries")
unique_countries = response.json()
selected_country = st.selectbox("Select a country", unique_countries)

# Send a GET request 
response = requests.get(f"http://127.0.0.1:8000/latest_data/{selected_country}")
data = response.json()


st.write(f"Country: {data['Country']}")
st.write(f"Code: {data['Code']}")
st.write(f"Population(2022): {data['Population(2022)']}")
st.write(f"% of World: {data['% of World']}")
st.write(f"CO2 emission (Tons): {data['CO2 emission (Tons)']}")

request = requests.get("http://127.0.0.1:8000/total_co2_2022")
total = float(request.json())
st.write(f"total CO2 emitted worldwide in 2022: {total}")

percent_of_co2_for_2022 = round((data['CO2 emission (Tons)'] * 100) / total, 2)
st.write(f"<h1>{selected_country} has participated for {percent_of_co2_for_2022}% of the total amount of CO2 emitted in 2022</h1>", unsafe_allow_html=True)
