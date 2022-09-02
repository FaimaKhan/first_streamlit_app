import streamlit
import pandas
import requests
streamlit.title ('Talk Of The Town - Homestyle Cooking')
streamlit.header('Breakfast Menu')
streamlit.text('🥞Pancake🥞')
streamlit.text('🧇 Waffle 🧇')
streamlit.text('🍳Eggs🍳')
streamlit.text('🥤 Fresh Orange Juice 🥤')
streamlit.text('🍌🥭🍑🍓Fruit Bowl 🍑🍓')
streamlit.header('🥒 🥗 Make Your Own Smoothie 🍍🍌')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Banana', 'Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
# New section to show response
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#Just writes the data to screen
#streamlit.text(fruityvice_response.json())
# Normalize the data 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Present data in a tabular form
streamlit.dataframe(fruityvice_normalized)
