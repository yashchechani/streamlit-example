import sys
import streamlit as st
import json
import pandas as pd 
import snowflake.connector
from datetime import datetime
import datetime as dt
import pytz
#  map chart
import pydeck as pdk

# for data frame tables display
from st_aggrid import AgGrid as stwrite
from st_aggrid.grid_options_builder import GridOptionsBuilder
# for role chart
import graphviz as graphviz
#annoated text
from annotated_text import annotated_text as atext


def create_session():    
       conn = snowflake.connector.connect(**st.secrets["snowflake"])          
       return conn
curr_sess = create_session()

asof_time = st.slider(
            "When do you want to go back in time for table "+curr_table,
            value=end_date,
            max_value=end_date,
            min_value=table_created,
            step=dt.timedelta(minutes=1),
            format="MM/DD/YY - HH:mm")
