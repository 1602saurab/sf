from dotenv import load_dotenv 
load_dotenv()   ### load all our enviornment variables 


import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 

model = genai.GenerativeModel("gemini-pro") 

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text 


##for UI we use Streamlit 

st.set_page_config(page_title="Lavish Chatbot") 
st.header("Lavish Smartbot") 
input = st.text_input("Input :" , key = "input") 
submit = st.button("Ask the Question:") 


if submit:
    response = get_gemini_response(input) 
    st.subheader("The Response is") 
    st.write(response) 

    