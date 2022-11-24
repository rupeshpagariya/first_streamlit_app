import streamlit
import pandas
streamlit.title('Tital changed! from Rupesh')

streamlit.header('Learning Snowflake')

streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.text('Metadata layer')
streamlit.text('Virtual warehouse')
streamlit.text('Storage')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


