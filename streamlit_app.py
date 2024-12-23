# Biblioteca streamlit para o chat app
import streamlit as st

# Integração e configuração do modelo Gemini
import google.generativeai as genai

client = genai.configure(api_key="AIzaSyA1VWXJB4DZh6TRwmCvUOS9jE4ZkAjxyks")
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Fluxo do chatbot
st.title("Gemini SIMILAR")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Qual o seu interesse?"):
     st.session_state.messages.append({"role": "user", "content": prompt})
     with st.chat_message("user"):
        st.markdown(prompt)
     response = model.generate_content(prompt, stream=True)
     complete_response = ''
     for stream in response:
        if stream.text:
           print(stream.text, end='', flush=True)
           complete_response += stream.text
     st.write(complete_response)
     st.session_state.messages.append({"role": "assistant", "content": complete_response})