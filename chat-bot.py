import streamlit as st
import openai
from datetime import datetime
import os

from src.functions import chat

# user input history
if "user_input_hist" not in st.session_state:
    st.session_state.user_input_hist = []
if "chatbot_response_hist" not in st.session_state:
    st.session_state.chatbot_response_hist = []

# get openai api key from environment variable
#open_ai_api_key = os.environ.get("OPEN_AI_API_KEY")
from creds import open_ai_api_key
openai.api_key = open_ai_api_key

# current date
current_date = datetime.today().strftime('%Y-%m-%d')

# user input
user_input = st.text_input("Enter your message")

# chatbot response if button is pressed
if user_input:
    st.session_state.user_input_hist.append(user_input)
    # chatbot response
    chatbot_response = chat(
        openai, 
        user_input, 
        st.session_state.user_input_hist, 
        st.session_state.chatbot_response_hist,
        current_date
    )
    st.session_state.chatbot_response_hist.append(chatbot_response)

    st.write(chatbot_response)
