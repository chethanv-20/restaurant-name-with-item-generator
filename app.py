import streamlit as st
import langchain_helper

st.title("Restaurant Name and menu generator")

cuisine = st.sidebar.selectbox("Pick a state", ("KARNATAKA", "TAMIL NADU", "ANDHRA PRADESH", "KERALA"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Recommended Menu Items**")
    for item in menu_items:
        st.write("-", item)

