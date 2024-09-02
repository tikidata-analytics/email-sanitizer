import streamlit as st
import pandas as pd
import re,os
from function import * 

# Set the page configuration with the new app name
st.set_page_config(
    page_title="Tikidata Email Sanity Checker", 
    page_icon="📧"
)
st.title("📧 Tikidata Email Sanity Checker")
with st.sidebar:
    st.title("Tikidata Analytics Email Sanity Checker")
    url = 'https://linktr.ee/tikidata_analytics'
    st.write(f"Feel free to [reach us out]({url}) should you need a customize Data Web App applications by visiting the following link:")
    

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls","csv"])
if uploaded_file:
    # Get the file extension
    filename = uploaded_file.name
    file_extension = os.path.splitext(filename)[1]  # Extracts the file extension, e.g., '.xlsx'
    st.write(f"Uploaded file extension: {file_extension}")
    read_functions = {
        '.xlsx': pd.read_excel,
        '.xls': pd.read_excel,
        '.csv': pd.read_csv
    }

    # Read the file using the appropriate pandas function
    df = read_functions[file_extension](uploaded_file) if file_extension in read_functions else None
    if df is not None:
         selected_column = st.selectbox("Select Email column:", df.columns)
    is_email = is_email_column(df,selected_column)

    if is_email:
        df_data = df[[selected_column]]
        sanity = email_sanity_check(df_data,selected_column)
        
    else:
        st.error(f"Column '{selected_column}' doesn't contains email ")

    
    
