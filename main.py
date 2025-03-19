import streamlit as st
import json
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.llms.groqllm import GroqLLM
from src.langgraphagenticai.graphs.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayREsultStreamlit




def load_langgraph_agenticai_app()
    #Load Ui
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    #text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message=st.session_state.timeframe
    else:
        user_message= st.chat_input('Enter your message')
    
    if user_message:
        try:
            #configure llm
            obj_llm_config=GroqLLM(user_control_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error('Error: LLM model could not be initialised')
                return
            
            #initilise and set up graph based on use case
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Error:No use case selected")
                return
            
            #GraphBuilder
            graph_builder=GraphBuilder(model)

            try:
                graph=GraphBuilder.setup_graph(usecase)
                DisplayREsultStreamlit(usecase,graph,user_message).display_reult_on_ui()
            except Exception as e:
                st.error(f"Error: Graph sertup Failed - {e}")
                return

        
        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")

            

        