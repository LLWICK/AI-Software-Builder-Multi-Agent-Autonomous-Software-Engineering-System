from langgraph.graph import START, END, StateGraph
from states import agent_state
from langchain_groq import ChatGroq
from prompts import planner_agent_prompt
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(model="openai/gpt-oss-120b")


def planner_agent(state: agent_state)-> agent_state:
    
    print("Executing Planner Agent Node....")

    query = planner_agent_prompt(state['user_query'])
  
    return {
        "plan": llm.invoke(query)
    }


def coding_agent(state: agent_state)-> agent_state:
    
    print("Executing Planner Agent Node....")

    query = planner_agent_prompt(state['user_query'])
  
    return {
        "plan": llm.invoke(query)
    }

builder = StateGraph(agent_state)

builder.add_node("planner_agent_node", planner_agent)

builder.add_edge(START,"planner_agent_node" )
builder.add_edge("planner_agent_node",END)

graph = builder.compile()

result = graph.invoke({"user_query": "Build a web based hang man"})

response = result['plan'].content

print(response)
