import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import io
import base64

def parse_html(file_content):
    soup = BeautifulSoup(file_content, 'html.parser')
    rows = soup.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols) # Keeping empty values
    return data

def get_table_download_link(df):
    # Convert dataframe to CSV for download
    csv = df.to_csv(index=False, encoding='utf-8-sig')
    b64 = base64.b64encode(csv.encode('utf-8-sig')).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download CSV file</a>'
    return href

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

    # Add a download link for the dataframe
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
