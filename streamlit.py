import streamlit as st
from gemini import gemini

st.title("cTACIA")
GEMINI_API_KEY = st.text_input("Gemini API Key")

if GEMINI_API_KEY:
    if "model" not in st.session_state:
        st.session_state["model"] = gemini(GEMINI_API_KEY)
        
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # with st.chat_message("assistant"):
    #     prompt_parts = ["say hi"]
    #     response = st.session_state["model"].generate_content(prompt_parts)
    #     stream = st.write(response.text)
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            prompt_parts = [prompt]
            response = st.session_state["model"].generate_content(prompt_parts)
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
