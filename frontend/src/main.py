import os
import datetime
import streamlit as st
from dotenv import load_dotenv

from utils import fetch_data

load_dotenv()


st.set_page_config(
	page_title="Chicago Police Dashboard",
	page_icon="👮",
	layout="wide",
	initial_sidebar_state="expanded",
	menu_items={
		'Get Help': 'https://github.com/koosha-sangari/chicago-crimes-dashboard',
		'Report a bug': 'https://github.com/koosha-sangari/chicago-crimes-dashboard',
		'About': 'Choose your filters and check the crimes location on the map!'
	}
)

st.header('👮 Chicago Crimes Map')
with st.sidebar:
	st.title('Crimes Filter')

	primary_type = st.selectbox(
		"Type of Crime:",
		fetch_data(f"{os.environ.get('API_BASE_URL')}/crimes/primary_types")[0]
	)

	date = st.date_input(
		"Date of Crime:",
		datetime.date(2022, 10, 1)
	)

crimes_data, count = fetch_data(f"{os.environ.get('API_BASE_URL')}/crimes?date={date}&primary_type={primary_type}")

st.text(f"🔎 Found {count} {primary_type} on {date}")

st.map(data=crimes_data, zoom=10)
