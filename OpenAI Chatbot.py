import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# LangSmith Tracking (optional - for monitoring)
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Enhanced Q&A Chatbot With OPENAI"

# Initialize session state for chat history and conversations
if "conversations" not in st.session_state:
    st.session_state.conversations = {}  # Store all conversation threads
if "current_conversation_id" not in st.session_state:
    st.session_state.current_conversation_id = None
if "conversation_counter" not in st.session_state:
    st.session_state.conversation_counter = 0

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, engine, temperature, max_tokens, conversation_history=None):
    """
    Generate AI response using OpenAI through LangChain.
    
    Args:
        question: User's input question
        api_key: OpenAI API key
        engine: Model name (e.g., "gpt-4o")
        temperature: Creativity level (0.0-1.0)
        max_tokens: Maximum response length
        conversation_history: List of previous messages for context
    
    Returns:
        str: AI-generated response
    """
    try:
        # Initialize LLM with all parameters
        llm = ChatOpenAI(
            model=engine,
            api_key=api_key,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # Create output parser
        output_parser = StrOutputParser()
        
        # If conversation history exists, include it in the prompt
        if conversation_history and len(conversation_history) > 0:
            # Build messages with history
            messages = [
                ("system", "You are a helpful assistant. Please respond to the user queries.")
            ]
            
            # Add conversation history
            for msg in conversation_history[-10:]:  # Last 10 messages for context
                if msg["role"] == "user":
                    messages.append(("user", msg["content"]))
                elif msg["role"] == "assistant":
                    messages.append(("assistant", msg["content"]))
            
            # Add current question
            messages.append(("user", f"Question: {question}"))
            
            # Create prompt with history
            prompt_with_history = ChatPromptTemplate.from_messages(messages)
            chain = prompt_with_history | llm | output_parser
        else:
            # No history, use simple prompt
            chain = prompt | llm | output_parser
        
        # Invoke chain with question
        answer = chain.invoke({'question': question})
        
        return answer
    
    except Exception as e:
        return f"Error: {str(e)}. Please check your API key and try again."

def create_new_conversation():
    """Create a new conversation thread"""
    st.session_state.conversation_counter += 1
    new_id = f"chat_{st.session_state.conversation_counter}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    st.session_state.conversations[new_id] = {
        "messages": [],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "title": f"New Chat {st.session_state.conversation_counter}"
    }
    st.session_state.current_conversation_id = new_id
    return new_id

def get_conversation_title(messages):
    """Generate a title from the first user message"""
    if messages and len(messages) > 0:
        first_user_msg = next((msg["content"] for msg in messages if msg["role"] == "user"), None)
        if first_user_msg:
            # Use first 50 characters as title
            return first_user_msg[:50] + ("..." if len(first_user_msg) > 50 else "")
    return "New Chat"

# App Title
st.title("💬 Enhanced Q&A Chatbot With OpenAI")

# Sidebar for settings and conversation management
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Get API key from environment or sidebar
    api_key_from_env = os.getenv("OPENAI_API_KEY")
    if api_key_from_env:
        st.success("✅ Using API key from .env file")
        api_key = api_key_from_env
    else:
        api_key = st.text_input(
            "Enter your OpenAI API Key:", 
            type="password",
            help="Or set OPENAI_API_KEY in .env file"
        )
    
    # Model selection
    engine = st.selectbox(
        "Select OpenAI model",
        ["gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo"],
        help="Choose the model to use for responses"
    )
    
    # Response parameters
    temperature = st.slider(
        "Temperature", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.7,
        help="Controls randomness. Lower = more focused, Higher = more creative"
    )
    
    max_tokens = st.slider(
        "Max Tokens", 
        min_value=50, 
        max_value=2000,
        value=500,
        help="Maximum length of response (1 token ≈ 0.75 words)"
    )
    
    st.divider()
    
    # Conversation Management
    st.header("💬 Conversations")
    
    # New Chat button
    if st.button("➕ New Chat", use_container_width=True, type="primary"):
        create_new_conversation()
        st.rerun()
    
    # Display conversation list
    if st.session_state.conversations:
        st.subheader("Chat History")
        
        # Create list of conversation IDs with titles
        conversation_list = []
        for conv_id, conv_data in st.session_state.conversations.items():
            title = conv_data.get("title", get_conversation_title(conv_data["messages"]))
            conversation_list.append((conv_id, title, conv_data["created_at"]))
        
        # Sort by creation time (newest first)
        conversation_list.sort(key=lambda x: x[2], reverse=True)
        
        # Display conversations
        for conv_id, title, created_at in conversation_list:
            col1, col2 = st.columns([3, 1])
            with col1:
                # Highlight current conversation
                if conv_id == st.session_state.current_conversation_id:
                    st.button(
                        f"📌 {title}",
                        key=f"conv_{conv_id}",
                        use_container_width=True,
                        disabled=True
                    )
                else:
                    if st.button(
                        f"💬 {title}",
                        key=f"conv_{conv_id}",
                        use_container_width=True
                    ):
                        st.session_state.current_conversation_id = conv_id
                        st.rerun()
            
            with col2:
                if st.button("🗑️", key=f"delete_{conv_id}", help="Delete conversation"):
                    if conv_id in st.session_state.conversations:
                        del st.session_state.conversations[conv_id]
                    if st.session_state.current_conversation_id == conv_id:
                        if st.session_state.conversations:
                            st.session_state.current_conversation_id = list(st.session_state.conversations.keys())[0]
                        else:
                            st.session_state.current_conversation_id = None
                    st.rerun()
    
    st.divider()
    st.caption("💡 Tip: Set OPENAI_API_KEY in .env file for better security")

# Main chat interface
if not st.session_state.current_conversation_id:
    # No conversation exists, create one
    create_new_conversation()

# Get current conversation
current_conv = st.session_state.conversations[st.session_state.current_conversation_id]
messages = current_conv["messages"]

# Display conversation title
if messages:
    title = get_conversation_title(messages)
    if current_conv.get("title") != title:
        current_conv["title"] = title

# Display chat messages
chat_container = st.container()
with chat_container:
    if messages:
        for message in messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
    else:
        st.info("👋 Start a new conversation! Type a message below and click 'Send'.")

# User input area
st.divider()

# Create input area with button
col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "Type your message:",
        key="user_input",
        placeholder="Ask me anything...",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("📤 Send", use_container_width=True, type="primary")

# Process user input when button is clicked or Enter is pressed
if send_button or (user_input and user_input.strip()):
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API Key in the sidebar or set OPENAI_API_KEY in .env file")
    elif user_input.strip():
        # Add user message to conversation
        user_message = {
            "role": "user",
            "content": user_input.strip(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        messages.append(user_message)
        
        # Update conversation title if it's the first message
        if len(messages) == 1:
            current_conv["title"] = get_conversation_title(messages)
        
        # Display user message
        with st.chat_message("user"):
            st.write(user_input.strip())
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Get conversation history (excluding current message for context)
                history = messages[:-1] if len(messages) > 1 else None
                
                response = generate_response(
                    user_input.strip(),
                    api_key,
                    engine,
                    temperature,
                    max_tokens,
                    conversation_history=history
                )
                
                st.write(response)
        
        # Add assistant response to conversation
        assistant_message = {
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        messages.append(assistant_message)
        
        # Rerun to refresh the page (input will be cleared automatically)
        st.rerun()

# Display conversation stats in sidebar
if messages:
    with st.sidebar:
        st.divider()
        st.caption(f"💬 Messages: {len(messages)}")
        st.caption(f"📅 Created: {current_conv['created_at']}")

