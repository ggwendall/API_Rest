import requests
import streamlit as st

# Create a dropdown menu to select the country
response = requests.get(f"http://127.0.0.1:8000/unique_countries")
unique_countries = response.json()
selected_country = st.selectbox("Select a country", unique_countries)

if st.button("delete Document"):
    # Send a DELETE request to the country endpoint for the selected country
    response = requests.delete(f"http://127.0.0.1:8000/delete_document/{selected_country}")

    data = response.json()
    if 'message' in data:
        st.write(data['message'])