import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
      streamlit.error ('Please select a fruit to get information.') 
   else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
except URLError as e:
   streamlit.error()
#Don't run anything past here - trying to debug
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
# Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
#Broken code
my_cur.execute ("Insert into fruit_load_list values ('from streamlight')")
