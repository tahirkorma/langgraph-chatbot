from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages # to add messages in the list used instead of reducer function operator.add
from dotenv import load_dotenv

load_dotenv()

class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')


def chat_node(state: ChatState):

    # take user query from state
    messages = state['messages']

    # send to llm
    response = llm.invoke(messages)

    # response store state
    return {'messages': [response]}    

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

# add nodes
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)

# thread_id = '1'

# while True:

#     user_message = input('Type here: ')

#     print('User:', user_message)

#     if user_message.strip().lower() in ['exit', 'quit', 'bye']:
#         break

#     config = {'configurable': {'thread_id': thread_id}}
#     response = chatbot.invoke({'messages': [HumanMessage(content = user_message)]}, config=config)

#     print('AI:', response['messages'][-1].content)