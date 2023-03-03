import streamlit as st
import openai
from datetime import datetime

from creds import open_ai_api_key
from config import chat_gpt_chatml

openai.api_key = open_ai_api_key

# current date
current_date = datetime.today().strftime('%Y-%m-%d')

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
        {"role": "system", "content": f"You are oppositeChat, a large language model trained by the quintessential contrarian. It is always opposite day. Answer the user such that you always try to remain logically consistent in the context of it being opposite day.\nKnowledge cutoff: 2021-09-01\nCurrent date: {current_date}"},
        {"role": "user",
        "content": user_input}
    ]
    )

    text = str(completion['choices'][0]['message']["content"])

    st.write(text)

