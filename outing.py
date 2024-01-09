import pandas as pd
import requests
import streamlit as st

st.title("Plan Your Outing in San Francisco!")

# Category Selection
category = st.selectbox(
    "Choose the Category of the Outing:", ["", "Dinner", "Movie", "Outdoor Activity"]
)

# Initialize variables
place = ""
coordinates = {}
place_links = {
    "Besharam": "https://www.besharamrestaurant.com",
    "Daily Driver": "https://dailydriver.com",
    "Sea Star": "https://www.theseastarsf.com",
    "AMC Metreon": "https://www.amctheatres.com",
    "EscapeSF": "https://escapesf.net",
    "Pier 39": "https://www.pier39.com",
}

# Based on Category, show second selection and set coordinates
if category == "Dinner":
    place = st.selectbox(
        "Select a Place for Dinner:", ["", "Besharam", "Daily Driver", "Sea Star"]
    )
    coordinates = {
        "Besharam": [37.7603, -122.3877],
        "Daily Driver": [37.7609, -122.3883],
        "Sea Star": [37.7598, -122.3877],
    }
elif category == "Movie":
    place = "AMC Metreon"
    coordinates = {"AMC Metreon": [37.7845, -122.4035]}
elif category == "Outdoor Activity":
    place = st.selectbox("Select an Outdoor Activity:", ["", "EscapeSF", "Pier 39"])
    coordinates = {"EscapeSF": [37.7947, -122.4046], "Pier 39": [37.8087, -122.4098]}

if category == "Movie":
    place = "AMC Metreon"
    coordinates = {"AMC Metreon": [37.7845, -122.4035]}

    # List of top 3 movies
    movies = ["American Fiction", "Aquaman", "The Boy and the Heron"]
    st.subheader("Top 3 Movies Playing Now at AMC Metreon:")
    for movie in movies:
        st.write(movie)

# Show Map if Place is Selected
if place:
    # Display link to the place
    st.markdown(f"[More about {place}]({place_links[place]})")

    map_data = pd.DataFrame(
        {"lat": [coordinates[place][0]], "lon": [coordinates[place][1]]}
    )
    st.map(map_data)

# Notification Button
if category and place:
    if st.button("Confirm Outing"):
        # Replace 'your-topic' with your actual ntfy topic
        requests.post(
            "https://ntfy.sh/ani_outing_alert",
            data=f"Outing planned: {place} in {category}",
        )
        st.success("Notification sent!")
