from langgraph.graph.message import add_messages
from typing import Annotated, TypedDict

class agent_state(TypedDict):
    messages: Annotated[list,add_messages]