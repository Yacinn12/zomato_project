import pandas as pd
import numpy as np
from tools import * 

st.set_page_config(
    page_title="Zomato Dashboard ", 
    page_icon=":bar_chart:", 
    layout="wide")

df_food = import_data("./datasets/food.xlsx")
# df_menu = import_data("./datasets/menu.xlsx")
# df_orders_Type = import_data("./datasets/orders_Type.xlsx") 
# df_orders = import_data("./datasets/orders.xlsx") 
df_restaurant = import_data("./datasets/restaurant.xlsx") 
# df_users = import_data("./datasets/users.xlsx") 


def clean_datasets():
  df_food.dropna(axis=0 ,how="all", inplace=True)
  df_menu["r_id"] = df_menu["r_id"].astype("str")
  df_menu.dropna(axis=0 ,how="any", inplace=True)
  df_orders["user_id"]=df_orders["user_id"].astype("str")
  df_orders["r_id"]=df_orders["r_id"].astype("str")
  df_orders["user_id"]=df_orders["user_id"].astype("str")
  df_orders["r_id"]=df_orders["r_id"].astype("str")
  df_restaurant["r_id"] = df_restaurant["r_id"].astype("str")
  df_restaurant["rating"] = df_restaurant["rating"].replace('--', np.nan).astype("float")
  mean_rating =df_restaurant["rating"].mean()
  df_restaurant["rating"].fillna(mean_rating, inplace=True)
  df_restaurant.dropna(axis=0 ,how="any", inplace=True)
  df_users["user_id"] = df_users["user_id"].astype("str")



 


#calculate the total number of orders
# total_orders = df_orders.shape[0]

# # Calculate the time period (in days) covered by the data
# start_date = df_orders['order_date'].min()
# end_date = df_orders['order_date'].max()
# time_period = (end_date - start_date).days

# # Calculate the overall purchase frequency
# overall_frequency = total_orders / time_period

# # print(f"La fréquence globale d'achat est de {overall_frequency:.2f} commandes par jour.")

# # Merge 'users' and 'orders' dataframes on 'user_id'
# user_orders = pd.merge(df_users, df_orders, on='user_id')

# # Group the merged dataframe by user name and count the number of orders
# user_order_counts = user_orders.groupby('user_name')['order_date'].count().sort_values(ascending=False)

# # Get the top 10 users with the most orders
# top_10_users = user_order_counts.head(10)

# print("The top 10 users who place the most orders are:")
# for user_name, count in top_10_users.items():
#   print(f"{user_name}: {count} orders")
  

# # Pour l'instant, supposons que la colonne 'item' contient des informations sur les garnitures

# #  faire un merge de food et menu avec f_id comme cle

# food_menu = pd.merge(df_food, df_menu, on='f_id')
# food_menu.head()
# topping_combinations = food_menu[food_menu['cuisine'].str.lower().str.contains("pizza")]['item'].value_counts()
# popular_topping_combinations = topping_combinations.head(10)
# print("\nLes combinaisons de garnitures les plus appréciées sont:\n", popular_topping_combinations)

# #  Comparer les performances des restaurants,

# # Merge orders and restaurants on 'r_id' and 'id' respectively
# orders_restaurants = pd.merge(df_orders, df_restaurant, left_on='r_id', right_on='r_id')

# # Merge the result with menu on 'r_id'
# orders_restaurants_menu = pd.merge(orders_restaurants, df_menu, on='r_id')

# orders_restaurants_menu.head()

# # Merge orders, restaurants, and menu dataframes
# orders_restaurants_menu = pd.merge(orders_restaurants, df_menu, left_on='r_id', right_on='r_id')

# # Calculate total revenue for each restaurant
# restaurant_revenue = orders_restaurants_menu.groupby('r_name')['price'].sum().sort_values(ascending=False)

# # Calculate average order value for each restaurant
# restaurant_avg_order_value = orders_restaurants_menu.groupby('r_name')['price'].mean().sort_values(ascending=False)

# # Calculate number of orders for each restaurant

# restaurant_order_counts = orders_restaurants_menu.groupby('r_name')['order_date'].count().sort_values(ascending=False)

# # Print top 10 restaurants by revenue, average order value, and number of orders
# print("Top 10 Restaurants by Revenue:")
# print(restaurant_revenue.head(10))

# print("\nTop 10 Restaurants by Average Order Value:")
# print(restaurant_avg_order_value.head(10))

# print("\nTop 10 Restaurants by Number of Orders:")
# print(restaurant_order_counts.head(10))

# # les 10 régions avec le plus de vente

# # Merge orders, restaurants, and menu dataframes
# orders_restaurants_menu = pd.merge(orders_restaurants, df_menu, left_on='r_id', right_on='r_id')

# # Calculate total revenue for each city
# city_revenue = orders_restaurants_menu.groupby('city')['price'].sum().sort_values(ascending=False)

# # Get the top 10 cities with the most revenue
# top_10_cities_revenue = city_revenue.head(10)

# print("Les 10 régions avec le plus de vente:")
# for city, revenue in top_10_cities_revenue.items():
#   print(f"{city}: {revenue} ")
  
  
  
  


st.header("Zomato Dashboard Projet ", divider=True)
st.subheader("Zomato Sales Analytics")


with st.sidebar:
  st.image("./assets/Zomato-Logo.png")
  
  st.write("Options de filtre")



  
      