import streamlit as st
import pandas as pd
import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import time
from datetime import datetime
import json


g_credentials = st.secrets["google_auth"]
cred = dict(g_credentials) 
# Google Sheets Authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_dict( cred, scope)
gc = gspread.authorize(credentials)


# Load Google Sheet data
sheet_url = cred.get("spreadsheet")
spreadsheet = gc.open_by_url(sheet_url)
worksheet = spreadsheet.worksheet("stash")
data = worksheet.get_all_records()
df = pd.DataFrame(data)



# Print results.

cat=st.radio('Stash - PandeAkshat', ['All','Core','Research', 'Social', 'Resource', 'LLM', 'Courses'], horizontal=True)

# Send a ping to confirm a successful connection
if cat=='All':
    for item in df.itertuples():
        col1, col2 = st.columns([4,1])
        with col1:
            with st.expander(item.title + ' ----- [' + item.category + ']'):
                st.write(item.information)
        with col2:
            st.link_button('Link', item.url)

if cat=='Core':
    for item in df.itertuples():
        if item.category=='Core':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)


if cat=='Research':
    for item in df.itertuples():
        if item.category=='Research':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)
if cat=='Social':
    for item in df.itertuples():
        if item.category=='Social':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)
if cat=='Resource':
    for item in df.itertuples():
        if item.category=='Resource':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)

if cat=='LLM':
    for item in df.itertuples():
        if item.category=='LLM':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)


if cat=='Courses':
    for item in df.itertuples():
        if item.category=='Courses':
            col1, col2 = st.columns([4,1])
            with col1:
                with st.expander(item.title + ' ----- [' + item.category + ']'):
                    st.write(item.information)
            with col2:
                st.link_button('Link', item.url)