import pandas as pd
import streamlit as st 

def is_email_column(df: pd.DataFrame, column_name: str) -> bool:
    """
    Check if the selected column in the DataFrame contains email addresses.

    Args:
    df (pd.DataFrame): The DataFrame to check.
    column_name (str): The name of the column to check.

    Returns:
    bool: True if the column contains valid email addresses, False otherwise.
    """
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,3}$'
    # Check if any value in the column matches the email pattern
    return df[column_name].astype(str).str.match(email_pattern).any()

def email_sanity_check(df: pd.DataFrame, column_name: str) -> dict:
    """
    Perform sanity checks on the email column and return results in a dictionary.

    Args:
    df (pd.DataFrame): The DataFrame containing the email data.
    column_name (str): The name of the column containing emails.

    Returns:
    dict: A dictionary with results of various sanity checks.
    """
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,3}$'
    
    # Extract the column with email data
    df_data = df[[column_name]].dropna()
    
    # Total number of emails
    total_emails = df_data.shape[0]
    
    # Count unique emails
    unique_emails = df_data[column_name].nunique()
    
    # Count valid emails
    valid_emails = df_data[column_name].str.match(email_pattern).sum()
    
    # Count emails per domain
    df_data['Domain'] = df_data[column_name].str.split('@').str[1]
    email_per_domain = df_data['Domain'].value_counts().to_dict()
    
    # Count emails by length
    df_data['Length'] = df_data[column_name].str.len()
    email_by_length = df_data['Length'].value_counts().to_dict()
    st.divider()
    st.subheader("Summary: ")
    st.success(f"Total email: {total_emails}")
    st.success(f"Total email with valid format: {valid_emails}")
    st.success(f"Total unique email: {unique_emails}")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Count email by domain:")
        st.bar_chart(email_per_domain
                     ,horizontal=True
                     ,x_label="Count Email"
                     ,y_label="Domain")
    with col2:
        st.write("Count email by length email:")
        st.bar_chart(email_by_length
                     ,horizontal=True
                     ,x_label="Count Email"
                     ,y_label="Length Email")


