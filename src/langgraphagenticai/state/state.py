from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_message
from typing import TypedDict, Annotated, List

class State(TypedDict):
    '''
    Represents the structure of the state used inthe graph
    '''

    messages: Annotated[list,add_messages]