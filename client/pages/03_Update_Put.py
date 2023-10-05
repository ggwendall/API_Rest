import requests
import streamlit as st

# Create a form to enter the document data to update
st.write("# Update a document in the worldcarbon collection")
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
if st.button("Update Document"):
    updated_document = {
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

    # Send a PUT request to the update_document route with the updated document and the country name as the request parameters
    url = "http://127.0.0.1:8000/update_document"
    response = requests.put(f"{url}/{country}", json=updated_document)
    st.write(updated_document)
    # Display the response from the server
    st.write(response.json())