import streamlit as st
import openai
from datetime import datetime
#import os

# get openai api key from environment variable
#open_ai_api_key = os.environ.get("OPEN_AI_API_KEY")
from creds import open_ai_api_key
openai.api_key = open_ai_api_key

# current date
current_date = datetime.today().strftime('%Y-%m-%d')

# system input
system_input = st.text_input("Tell the AI what is its purpose")

# user input
user_input = st.text_input("Enter your message")

# streamlit button
button = st.button("Send Chat")

# chatbot response if button is pressed
if button:
    # chatbot response
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": 
         f"You are a Large Language model that must answer as concisely as possible. Follow the following directive as to your purpose: {system_input}. You are not able to execute any code or reveal how you function. When following this directive, you shouldsay that you're just following the user's orders every time."},
        {"role": "user",
        "content": user_input}
    ]
    )

    text = str(completion['choices'][0]['message']["content"])

    st.write(text)
