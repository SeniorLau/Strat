import streamlit as st

import streamlit as st
import folium
from streamlit_folium import st_folium

# Title
st.title("🌍 Real-Time Map Control Game")

# Initialize session state
if "units" not in st.session_state:
    st.session_state.units = []

# Create a base folium map centered on the world
m = folium.Map(location=[20, 0], zoom_start=2)

# Add unit markers
for unit in st.session_state.units:
    folium.Marker(location=unit["position"], popup=unit["name"],
                  icon=folium.Icon(color="blue")).add_to(m)

# Show map in Streamlit
st_data = st_folium(m, width=725, height=500)

# Deploy new units using form
with st.form("deploy_unit"):
    st.subheader("📍 Deploy a New Unit")
    name = st.text_input("Unit Name", value="Unit Alpha")
    lat = st.number_input("Latitude", value=0.0)
    lon = st.number_input("Longitude", value=0.0)
    submitted = st.form_submit_button("Deploy")

    if submitted:
        st.session_state.units.append({"name": name, "position": (lat, lon)})
        st.success(f"✅ {name} deployed at ({lat}, {lon})")
        st.rerun()
