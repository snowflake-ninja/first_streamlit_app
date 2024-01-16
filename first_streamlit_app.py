import streamlit
import pandas
streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.title("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.title("🥗 kale, spinach & Rocket Smoothie")
streamlit.title("🐔 Hard-Boiled Free-Range Egg")
streamlit.title("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
