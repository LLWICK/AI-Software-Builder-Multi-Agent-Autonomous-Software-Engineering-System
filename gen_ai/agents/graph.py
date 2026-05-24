from langgraph.graph import START, END, StateGraph
from states import agent_state
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(model="openai/gpt-oss-120b")


def agent_node(state: agent_state)-> agent_state:
    
    print("Executing Agent Node....")
    return {
        "messages": llm.invoke(state['messages'][-1])
    }


builder = StateGraph(agent_state)

builder.add_node("agent_node", agent_node)

builder.add_edge(START,"agent_node" )
builder.add_edge("agent_node",END)

graph = builder.compile()

result = graph.invoke({"messages": "who is the president of US?"})

response = result['messages'][-1].content

print(response)
