import streamlit as st

def translate_state(user_input: list, chatbot_response: list):
    user_messages = [{"role": "user",
                       "content": user_input[i]} for i in range(len(user_input))]
    chatbot_messages = [{"role": "assistant", 
                         "content": chatbot_response[i]} for i in range(len(chatbot_response))]
    
    messages = user_messages + chatbot_messages
    return messages

@st.cache_data
def chat(openai, user_input, user_input_hist, chatbot_response_hist, current_date):
    system_messages = [ {"role": "system", "content": f"You are oppositeChat, a large language model trained by the quintessential contrarian. It is always opposite day. Answer the user such that you always try to remain logically consistent in the context of it being opposite day.\nKnowledge cutoff: 2021-09-01\nCurrent date: {current_date}"}]

    state_messages = translate_state(user_input_hist, chatbot_response_hist)

    user_input = [{"role": "user", "content": user_input}]

    messages = system_messages + state_messages + user_input

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )

    return str(completion['choices'][0]['message']["content"])
