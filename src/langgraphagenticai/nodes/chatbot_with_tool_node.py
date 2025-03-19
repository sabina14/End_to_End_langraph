from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    '''
    Chatbot logic enhanced with tool integration
    '''

    def __init__(self,model):
        
        self.llm = model
    
    def process(self, state: State)->dict:
        '''
        Process the input state and generate a response with tool integration.
        '''
        user_input = state["message"]["-1"] if state["messages"] else ""

        llm_response = self.llm.invoke([{"role":"user","content": user_input}])

        #simulate tool-specific logic
        tools_reponse = f"Tools integration for :'{user_input}'"

        return {'messages':[llm_response, tools_reponse]}
    
    def create_chatbot(self,tools):
        '''
        returns a chatbot node function'''

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            '''
        Chatbot logic for processing state'''

            return {"message": [llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node