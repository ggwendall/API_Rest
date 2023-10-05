import requests
import streamlit as st

# Create a form to enter the new document
st.write("# Add a new document to the worldcarbon collection")
country = st.text_input("Country")
code = st.text_input("Code")
calling_code = st.text_input("Calling Code")
year = st.number_input("Year", value=2022)
co2_emission = st.number_input("CO2 emission (Tons)", value=0)
population = st.number_input("Population(2022)", value=0)
area = st.number_input("Area", value=0)
percent_of_world = st.number_input("% of World", value=0.0)
density = st.text_input("Density(km2)")

# Create a button to submit the form
if st.button("Add Document"):
    new_document = {
        "Country": country,
        "Code": code,
        "Calling Code": calling_code,
        "Year": year,
        "CO2 emission (Tons)": co2_emission,
        "Population(2022)": population,
        "Area": area,
        "% of World": percent_of_world,
        "Density(km2)": density
    }

    # Send a POST request to the add_document route with the new document as the request body
    url = "http://127.0.0.1:8000/add_document"
    response = requests.post(url, json=new_document)
    st.write(new_document)
    # Display the response from the server
    st.write(response.json())