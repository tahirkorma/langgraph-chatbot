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

    response  = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    ai_message = response['messages'][-1].content
    # second add the message to the message history
    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
         st.text(ai_message)         