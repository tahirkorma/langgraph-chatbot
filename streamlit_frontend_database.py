import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langgraph_database_backend import chatbot, retrieve_all_threads
import uuid

# *********************************************** Utility functions*************************************************

def generate_thread_id():
     thread_id = uuid.uuid4()
     return thread_id

def reset_chat():
     thread_id = generate_thread_id()
     st.session_state['thread_id'] = thread_id
     add_thread(thread_id)
     st.session_state['message_history'] = []
     st.session_state['chat_titles'][thread_id] = "New chat"

def add_thread(thread_id):
     if thread_id not in st.session_state['chat_threads']:
          st.session_state['chat_threads'].append(thread_id) 

def load_conversation(thread_id):
     
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    # Check if messages key exists in state values, return empty list if not
    return state.values.get('messages', [])          

# *********************************************** Session setup********************************************************

if 'message_history' not in st.session_state:
     st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
     st.session_state['thread_id'] = None

if 'chat_threads' not in st.session_state:
     st.session_state['chat_threads'] = retrieve_all_threads()

if 'chat_titles' not in st.session_state:
     st.session_state['chat_titles'] = {}
    

if st.session_state['thread_id'] is not None:
    add_thread(st.session_state['thread_id'])
    if st.session_state['thread_id'] not in st.session_state['chat_titles']:
         st.session_state['chat_titles'][st.session_state['thread_id']] = "New chat"


# *********************************************** Sidebar UI********************************************************

st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
     reset_chat()


st.sidebar.header('Chats')

for thread_id in st.session_state['chat_threads'][::-1]:
     title = st.session_state["chat_titles"].get(thread_id, str(thread_id))
     if st.sidebar.button(title, key=thread_id):
          st.session_state['thread_id'] = thread_id
          messages = load_conversation(thread_id)

          temp_messages = []

          for msg in messages:
               if isinstance(msg, HumanMessage):
                    role = 'user'
               else:
                    role = 'assistant'
               temp_messages.append({'role': role, 'content': msg.content})

          st.session_state['message_history'] = temp_messages              
                                      

# load converstion history
for message in st.session_state['message_history']:
     with st.chat_message(message['role']):
          st.text(message['content'])

#  {'role':'user', 'content': 'Hi'}
#  {'role':'assistant', 'content': 'Hello'}

# CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

CONFIG = {
     'configurable': {'thread_id': st.session_state['thread_id']},
     'metadata':{
     'thread_id': st.session_state['thread_id']
     },
     'run_name': "chat_turn",
}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to the message history
    st.session_state['message_history'].append({'role':'user', 'content': user_input})
    with st.chat_message('user'):
         st.text(user_input)

    # update chat titles
    current_thread = st.session_state["thread_id"]
    if st.session_state["chat_titles"].get(current_thread, "New chat") == "New chat":
         st.session_state["chat_titles"][current_thread] = user_input[:30] + ("..." if len(user_input) > 30 else "")
   
    # second add the message to the message history
    
    with st.chat_message('assistant'):
    
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content = user_input)]},
                config =  CONFIG,
                stream_mode = 'messages'
            )      
        )
    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})        