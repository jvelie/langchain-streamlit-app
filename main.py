import langchain_helper as lch
import streamlit as st

st.title("Pet's name generator")

user_animal_type = st.sidebar.selectbox("What pet do you have?", ("Cat","Dog","Cow","Hamster"))

user_pet_color = st.sidebar.text_area(label=f"What color is your {user_animal_type}?", max_chars=15).lower()

if user_pet_color:
    response = lch.generate_pet_name(user_animal_type,user_pet_color)
    st.text(response['pet_name'])

#if user_animal_type == "Cat":
#    user_pet_color = st.sidebar.text_area(label="What color is your cat?",
#    max_chars=15)
#
#if user_animal_type == "Dog":
#    user_pet_color = st.sidebar.text_area(label="What color is your dog?",
#    max_chars=15)
#
#if user_animal_type == "Cow":
#    user_pet_color = st.sidebar.text_area(label="What color is your cow?",
#    max_chars=15)
#
#if user_animal_type == "Hamster":
#    user_pet_color = st.sidebar.text_area(label="What color is your hamster?",
#    max_chars=15)
