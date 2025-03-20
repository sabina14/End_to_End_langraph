from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    '''returns llist pf tools to be used in chatbot'''

    tools=(TavilySearchResults)

    return tools

def create_tools_node(tools):
    ''' creates and returns a tool node for the graph'''

    return ToolNode(tools=tools)
