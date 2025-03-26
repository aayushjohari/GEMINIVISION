import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

ai_api_key=os.getenv("GOOGLE_APT_KEY")

genai.configure(api_key=ai_api_key)


def get_gemini_response(input_message,input_image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input_message != "": 
        response = model.generate_content([input_message,input_image])
    else: 
        response = model.generate_content(input_image)
    return response.text

st.set_page_config(page_title ="generative ai based chatbot")
st.header("GEMINI BASED CHATBOT ")

input = st.text_input("Input prompt :" , key ="input")
uploaded_file = st.file_uploader("Choose an image : ", type =["jpeg" ,"jpg" ,"png"])




display_imageimage = ""
if uploaded_file is not None:
    display_image = Image.open(uploaded_file)
    st.image(display_image ,caption ="uploaded image")


submit = st.button("SUBMIT")

if submit:
    output = get_gemini_response(input_message = input , input_image = display_image)
    st.subheader("your response is : ")
    st.write(output)