import streamlit as st
from streamlit_chat import message 
import numpy as np 
import random

st.set_page_config(
    page_title="Cat GPT",
    page_icon=":cat:"
)


st.sidebar.title("New Chats are not avilable")
st.sidebar.caption("You can type anything in the box and imagine its gonna do something.")
st.sidebar.text_area('')

st.image('catchat.png', width=150)
st.title("Cat GPT")
request = st.text_input("", key="input_text")

def return_meow ():
    array = []
    conta_meow = random.randint(1,7)

    array.append(' meow ' * conta_meow)
    global response
    response = ' '.join(str(e) for e in array)
    

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


user_input = request

if user_input:
    return_meow()

    st.session_state.past.append(user_input)
    st.session_state.generated.append(response)


if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1,-1):
        message(st.session_state["generated"][i], key=str(i),avatar_style='gridy')
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user',avatar_style='miniavs')
