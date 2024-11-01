import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Hotel data", page_icon="🏖")
#st.title(":orange[Easy]:blue[Monitor] 🏖")


# Use HTML within st.markdown to apply color styling
st.markdown("<h1 style='color: orange;'>Easy<span style='color: blue;'>Monitor</span> 🏖</h1>", unsafe_allow_html=True)

st.subheader("Discover the perfect soundtrack for every mood!")

st.markdown("""
Welcome to EasyMonitor – Your Comprehensive Hotel Booking Cancellation Monitoring Tool

""")

home_tab, data_tab, recommendations_tab = st.tabs(["Home", "Data", "Classification"])

home_tab.markdown("""
In the fast-paced travel industry, being aware of booking changes and cancellations is crucial to delivering outstanding service. EasyMonitor is designed specifically for tour agencies, giving you real-time insights into hotel booking cancellations. Our tool helps you stay one step ahead, allowing you to proactively manage changes, anticipate client needs, and minimize potential disruptions – all from one convenient dashboard.
""")

##data tab

@st.cache
def get_data():
    df = pd.read_csv("H1.csv")
    df = df.head(200)
    return df

df = get_data()
data_tab.dataframe(df)



