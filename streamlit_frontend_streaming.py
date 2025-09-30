import streamlit as st
from langchain_core.messages import HumanMessage
from langgraph_backend_chatbot import chatbot

st.set_page_config(page_title= "My AI Chatbot 🤖", page_icon="💬")
st.markdown(
    """
    <h2 style='text-align: center;'>
        💬 My AI Chatbot
    </h2>
    """,
    unsafe_allow_html=True
)

# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
     st.session_state['message_history'] = []

# message_history = [] not needed because we are using st.session_state

# load converstion history
for message in st.session_state['message_history']:
     with st.chat_message(message['role']):
          st.text(message['content'])

#  {'role':'user', 'content': 'Hi'}
#  {'role':'assistant', 'content': 'Hello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to the message history
    st.session_state['message_history'].append({'role':'user', 'content': user_input})
    with st.chat_message('user'):
         st.text(user_input)


    # second add the message to the message history
    
    with st.chat_message('assistant'):
    
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content = user_input)]},
                config =  {'configurable': {'thread_id': 'thread-1'}},
                stream_mode = 'messages'
            )      
        )
    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})        