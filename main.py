import pandas as pd 
import numpy as np
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.chart_container import chart_container
import matplotlib.pyplot as plt 
import plotly.express as px
from tools import import_data


st.set_page_config(
    page_title="Zomato Dashboard", 
    page_icon=":bar_chart:", 
    layout="wide")



def header():
    col1, col2 = st.columns([1,3])
    with col1:
        st.image("./assets/Zomato-Logo.png")

    with col2:
        st.title("zomato Dashboard Projet ")
        st.subheader("Zomato Sales Analytics")

def sidebar():

    with st.sidebar:

        st.image("./assets/Zomato-Logo.png")

        st.header("Dashboard Options")

        st.sidebar.subheader("Data")
        country=st.sidebar.selectbox(
            "SELECT filter one",
            options=("Food", "Menu", "Order","Restaurant","User","Order type"),
        )

        st.sidebar.subheader("Best Restaurant")
        year=st.sidebar.multiselect(
            "SELECT YEAR",
            options=[2018, 2019, 2020],
            default=[2018, 2019, 2020],
        )

        st.sidebar.subheader("Months")
        month=st.sidebar.multiselect(
            "SELECT MONTH",
            options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            default=[1, 2, 3, 4],
        )
        st.divider()

def metrics():
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(label="Mean Rating", value="3.89", delta="Rating")
    col2.metric(label="Total City", value="821", delta="All City")
    col3.metric(label="Best restaurant", value="Domino", delta="All Restaurant")
    col4.metric(label="Total Countries", value="5", delta="All countries")

    style_metric_cards()




def df_resto_cleaned():
    # df = pd.read_excel("./datasets/biling.xlsx" )
    df_restaurant = import_data("./datasets/restaurant.xlsx")
    df_restaurant["r_id"] = df_restaurant["r_id"].astype("str")
    df_restaurant["rating"] = df_restaurant["rating"].replace('--', np.nan).astype("float")
    mean_rating =df_restaurant["rating"].mean()
    df_restaurant["rating"].fillna(mean_rating, inplace=True)
    df_restaurant.dropna(axis=0 ,how="any", inplace=True)

    return df_restaurant

def datasets():

    df = df_resto_cleaned()
    with st.expander("View Dataset"):
        df_selected = st.multiselect("SELECT COLUMNS", df.columns, default=["city"])
        st.dataframe(df[df_selected])
    

def bar_chart():
    
    df = df_resto_cleaned()
    with chart_container(df):
        fig = px.bar(df, x="r_name", y="rating")

        fig.update_layout(
            xaxis_title="Ville",
            yaxis_title="Number of Rating",
            title="Category Orders",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            legend_title="city",
            legend_y=0.9
        )
        st.plotly_chart(fig)


if __name__ == "__main__":

    header()

    sidebar()

    with st.container():
        metrics()

        #datasets()

        #bar_chart()
        