import streamlit as st
from groq import Groq
from langchain.chains import ConversationChain, LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import datetime

# Set page config
st.set_page_config(
    page_title="AI Chat",
    page_icon="💫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom modern dark theme CSS
st.markdown("""
    <style>
    /* Global theme */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, #1a1a2e, #16213e);
        color: #e6e6e6;
    }
    
    .stTitle {
        display: none;
    }
    
    /* Custom header */
    .custom-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        color: #fff;
        font-size: 1.5rem;
        font-weight: 600;
    }
    
    .header-status {
        color: #4CAF50;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Chat container */
    .chat-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Message bubbles */
    .stChatMessage {
        background: transparent !important;
        border: none !important;
    }
    
    [data-testid="stChatMessageContent"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #e6e6e6 !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
    }
    
    /* User message specific */
    [data-testid="user-message"] [data-testid="stChatMessageContent"] {
        background: rgba(66, 135, 245, 0.1) !important;
        border-color: rgba(66, 135, 245, 0.2) !important;
    }
    
    /* Assistant message specific */
    [data-testid="assistant-message"] [data-testid="stChatMessageContent"] {
        background: rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Code blocks */
    code {
        background: rgba(0, 0, 0, 0.2) !important;
        color: #a6e22e !important;
        padding: 0.2rem 0.4rem !important;
        border-radius: 4px !important;
    }
    
    pre {
        background: rgba(0, 0, 0, 0.2) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Input area */
    .stTextInput {
        position: fixed;
        bottom: 2rem;
        left: 50%;
        transform: translateX(-50%);
        width: 80% !important;
        max-width: 800px;
    }
    
    .stTextInput > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(10px);
        padding: 0.5rem !important;
    }
    
    .stTextInput input {
        color: #fff !important;
    }
    
    /* Timestamp */
    .message-timestamp {
        font-size: 0.7rem;
        color: rgba(255, 255, 255, 0.5);
        margin-top: 0.5rem;
    }
    
    /* Welcome message */
    .welcome-container {
        text-align: center;
        margin-bottom: 2rem;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        backdrop-filter: blur(10px);
    }
    
    .welcome-title {
        color: #fff;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    .welcome-text {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    welcome_message = {
        "role": "assistant",
        "content": "Hello! I'm your AI assistant. How can I help you today?",
        "timestamp": datetime.datetime.now().strftime("%H:%M")
    }
    st.session_state.messages.append(welcome_message)

def initialize_chat():
    groq_api_key = "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"
    model = 'llama3-70b-8192'
    
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=model
    )
    
    system_prompt = """You are a helpful and engaging AI assistant. Provide clear, thoughtful responses while maintaining a natural conversational tone."""
    
    memory = ConversationBufferWindowMemory(k=10, memory_key="chat_history", return_messages=True)
    
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{human_input}")
    ])
    
    return LLMChain(
        llm=groq_chat,
        prompt=prompt,
        verbose=False,
        memory=memory,
    )

def main():
    # Custom header
    st.markdown("""
        <div class="custom-header">
            <div class="header-title">AI Chat</div>
            <div class="header-status">
                <span style="background: #4CAF50; width: 8px; height: 8px; border-radius: 50%; display: inline-block;"></span>
                Online
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    conversation = initialize_chat()
    
    # Chat container
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                st.markdown(f"<div class='message-timestamp'>{message['timestamp']}</div>", unsafe_allow_html=True)
    
    # Add space for fixed input box
    st.markdown("<div style='padding-bottom: 100px;'></div>", unsafe_allow_html=True)
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "timestamp": current_time
        })
        with st.chat_message("user"):
            st.markdown(prompt)
            st.markdown(f"<div class='message-timestamp'>{current_time}</div>", unsafe_allow_html=True)
        
        try:
            with st.chat_message("assistant"):
                with st.spinner(""):
                    response = conversation.predict(human_input=prompt)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response,
                        "timestamp": datetime.datetime.now().strftime("%H:%M")
                    })
                    st.markdown(response)
                    st.markdown(f"<div class='message-timestamp'>{datetime.datetime.now().strftime('%H:%M')}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error("I apologize, but I encountered an error. Please try again.")

if __name__ == "__main__":
    main()