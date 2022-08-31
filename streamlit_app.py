import streamlit
import pandas
streamlit.title ('Talk Of The Town - Homestyle Cooking')
streamlit.header('Breakfast Menu')
streamlit.text('🥞Pancake🥞')
streamlit.text('🧇 Waffle 🧇')
streamlit.text('🍳Eggs🍳')
streamlit.text('🥤 Fresh Orange Juice 🥤')
streamlit.text('🍌🥭🍑🍓Fruit Bowl 🍑🍓')
streamlit.header('🥒 🥗 Make Your Own Smoothie 🍍🍌')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
