import requests
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# Create a dropdown menu to select the country
response = requests.get(f"http://127.0.0.1:8000/unique_countries")
unique_countries = response.json()
selected_country = st.selectbox("Select a country", unique_countries)

# Send a GET request to the country endpoint for the selected country
response = requests.get(f"http://127.0.0.1:8000/country/{selected_country}")

# Convert the JSON response 
data = response.json()
df = pd.json_normalize(data)
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# create plot
df = df[["Year", "CO2 emission (Tons)"]]
df.set_index("Year", inplace=True)
fig, ax = plt.subplots()
sns.lineplot(data=df, x=df.index, y="CO2 emission (Tons)", ax=ax)
st.title(f"CO2 Emissions Over Time for {selected_country}")
st.write('In tons !')
ax.set_xlabel("Year")
ax.set_ylabel("CO2 Emissions (Tons)")
ax.set_xlim(df.index.min(), df.index.max())
# Add a slider to adjust the scale
y_max = st.slider("Select the maximum y-axis limit", 0, 60000000000, 60000000000, 1)
ax.set_ylim(0, y_max)
st.pyplot(fig)