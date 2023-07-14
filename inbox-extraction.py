!pip install streamlit pandas beautifulsoup4 openpyxl

import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import io

def parse_html(file_content):
    soup = BeautifulSoup(file_content, 'html.parser')
    rows = soup.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols) # Keeping empty values
    return data

# File uploader
html_file = st.file_uploader("Upload an HTML file", type=['html', 'htm'])

if html_file is not None:
    # File is uploaded, let's process it
    file_content = html_file.read()
    data = parse_html(file_content)

    df = pd.DataFrame(data, columns=['Unnamed: 1', 'Unnamed: 2', 'Viewed', 'Deleted', 'Cta', 'Start', 'End', 'Title', 'Campaign Name', 'Bonus Code', 'Unnamed: 3'])

    # Keep only the necessary columns
    df = df[['Viewed', 'Start', 'End', 'Title', 'Campaign Name']]

    # Display the DataFrame
    st.write(df)
