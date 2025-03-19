from langchain_community.tools.tavily_search import TavilySeaarchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    '''returns llist pf tools to be used in chatbot'''

    tools=(TavilySeaarchResults)

    return tools

def create_tools_node(tools):
    ''' creates and returns a tool node for the graph'''

    return ToolNode(tools=tools)
