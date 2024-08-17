import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the no of days to forecast")
option = st.selectbox("Select Data to View",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    d, t = get_data(int(days), place, option)

    if option == "Temperature":
        figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature(C)"})
        st.plotly_chart(figure)
    elif option == "Sky":
        paths = []
        for image in t:
            if image == 'Clouds':
                paths.append("images/cloud.png")
            elif image == "Rain":
                paths.append("images/rain.png")
            elif image == "Clear":
                paths.append("images/clear.png")
            elif image == "Snow":
                paths.append("images/snow.png")

        st.image(paths, width=115, caption=d)