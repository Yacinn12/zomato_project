import pandas as pd 
import streamlit as st


@st.cache_data
def import_data(path):
    try:
        return pd.read_excel(path)
    except FileNotFoundError as e:
        print("❌❌❌  Error File not found")
        return None
    except FileExistsError:
        print("❌❌❌  Error File not found")
        return None
    
