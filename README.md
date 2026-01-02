# 🤖 Chatbots Collection - Multi-LLM Chatbot Applications

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://python.langchain.com/)

A comprehensive collection of chatbot applications supporting multiple LLM providers (OpenAI, Ollama) with advanced features including web search, web scraping, chat history, and conversation management.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Available Chatbots](#available-chatbots)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## 🎯 Overview

This project provides production-ready chatbot applications with support for:

- **OpenAI Models** (GPT-4o, GPT-4, GPT-3.5-turbo)
- **Ollama Models** (Mistral, Llama3.2, Llama3.1, Gemma, and more)
- **Web Search & Scraping** capabilities
- **Chat History** and conversation management
- **Multiple Conversation Threads** (like ChatGPT)
- **Context-Aware Responses**

### What Problem Does It Solve?

1. **Unified Interface**: One codebase supporting multiple LLM providers
2. **Local & Cloud Options**: Use cloud (OpenAI) or local (Ollama) models
3. **Web-Enabled**: Search Google and scrape websites for current information
4. **Production-Ready**: Chat history, conversation threads, error handling
5. **Easy to Extend**: Modular design for adding new features

---

## ✨ Features

### Core Features

- ✅ **Multi-LLM Support**: OpenAI and Ollama
- ✅ **Chat History**: Maintains conversation context
- ✅ **Multiple Conversations**: Thread-based chat management
- ✅ **Web Search**: Google search integration
- ✅ **Web Scraping**: Extract content from websites
- ✅ **Model Selection**: Choose from available models
- ✅ **Context-Aware**: Uses conversation history for better responses
- ✅ **User-Friendly UI**: Streamlit-based interface

### Advanced Features

- ✅ **Automatic Model Detection**: Lists available Ollama models
- ✅ **Conversation Threads**: Multiple separate conversations
- ✅ **Query Editor**: Review/edit generated SQL (for SQL chatbot)
- ✅ **Error Handling**: Graceful fallbacks and error messages
- ✅ **LangSmith Integration**: Optional tracing and monitoring

---

## 🤖 Available Chatbots

### 1. **OpenAI Chatbot** (`OpenAI Chatbot.py`)
- **Basic chatbot** using OpenAI models
- Simple Q&A interface
- Model selection (GPT-4o, GPT-4, GPT-3.5-turbo)
- Temperature and token controls

### 2. **OpenAI Chatbot Enhanced** (`OpenAIChatbot_WEB_ENABLED.py`) ⭐ **Recommended**
- **Full-featured chatbot** with all enhancements
- Web search and scraping capabilities
- Chat history and conversation threads
- "Ask a Question" button
- Multiple conversation management
- LinkedIn profile search support

### 3. **Ollama Chatbot** (`OllamaChatbot.py`)
- **Basic local chatbot** using Ollama
- Simple interface
- Works offline

### 4. **Ollama Chatbot Enhanced** (`OllamaChatbot_ENHANCED.py`) ⭐ **Recommended**
- **Full-featured local chatbot**
- Automatic model detection
- Chat history
- "Ask a Question" button
- Model selection from available Ollama models

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) OpenAI API key
- (Optional) Ollama installed locally

### Step 1: Clone or Navigate to Project

```bash
cd "/home/srprabhala/Documents/Learning/Chatbots"
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# Required for OpenAI chatbot
OPENAI_API_KEY=your_openai_api_key_here

# Optional: For LangSmith tracking
LANGCHAIN_API_KEY=your_langchain_api_key_here

# Optional: For better web search (recommended)
SERPAPI_API_KEY=your_serpapi_key_here

# Optional: Custom Ollama URL (default: http://localhost:11434)
OLLAMA_BASE_URL=http://localhost:11434
```

### Step 5: (Optional) Install Ollama

For local models:

```bash
# Download from https://ollama.com
# Or install via package manager

# Start Ollama
ollama serve

# Pull some models
ollama pull mistral
ollama pull llama3.2
ollama pull llama3.1
```

---

## 🚀 Quick Start

### OpenAI Chatbot (Web-Enabled)

```bash
streamlit run OpenAIChatbot_WEB_ENABLED.py
```

**Features:**
- Web search and scraping
- Chat history
- Multiple conversations
- Model selection

### Ollama Chatbot (Enhanced)

```bash
streamlit run OllamaChatbot_ENHANCED.py
```

**Features:**
- Automatic model detection
- Chat history
- Local processing (no API keys needed)

---

## 📖 Usage Guide

### OpenAI Chatbot Enhanced

#### 1. **Start the Application**
```bash
streamlit run OpenAIChatbot_WEB_ENABLED.py
```

#### 2. **Configure Settings**
- **API Key**: Enter OpenAI API key (or set in `.env`)
- **SerpAPI Key**: Optional, for better Google search
- **Model**: Select GPT-4o, GPT-4-turbo, GPT-4, or GPT-3.5-turbo
- **Enable Web Tools**: Toggle web search/scraping

#### 3. **Start a Conversation**
- Click "➕ New Chat" to create a new thread
- Type your question
- Click "📤 Send" or press Enter

#### 4. **Use Web Features**
Ask questions like:
- "What's the latest news about AI?"
- "Find Srinivasa Murthy Prabhala on LinkedIn"
- "Scrape content from https://example.com"

#### 5. **Manage Conversations**
- Switch between conversations in sidebar
- Delete conversations with 🗑️ button
- Each conversation maintains its own history

### Ollama Chatbot Enhanced

#### 1. **Start Ollama**
```bash
ollama serve
```

#### 2. **Pull Models** (if not already done)
```bash
ollama pull mistral
ollama pull llama3.2
```

#### 3. **Run the Application**
```bash
streamlit run OllamaChatbot_ENHANCED.py
```

#### 4. **Select Model**
- App automatically lists available models
- Select from dropdown
- Model info shown in expander

#### 5. **Chat**
- Type question
- Click "❓ Ask a Question" or press Enter
- Chat history maintained automatically

---

## 📁 Project Structure

```
Chatbots/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .env                               # Environment variables (create this)
│
├── OpenAI Chatbot.py                  # Basic OpenAI chatbot
├── OpenAIChatbot_WEB_ENABLED.py       # ⭐ Enhanced OpenAI chatbot (web-enabled)
├── OpenAIChatbot_IMPROVED.py          # Improved version (no web features)
├── OpenAIChatbot_EXPLAINED.md         # Detailed code explanation
│
├── OllamaChatbot.py                   # Basic Ollama chatbot
├── OllamaChatbot_ENHANCED.py          # ⭐ Enhanced Ollama chatbot
│
├── Documentation/
│   ├── ENHANCEMENTS_GUIDE.md          # Chat history & threads guide
│   ├── WEB_FEATURES_GUIDE.md          # Web search & scraping guide
│   ├── OLLAMA_CHATBOT_GUIDE.md        # Ollama chatbot guide
│   ├── QUICK_SETUP_WEB.md             # Quick web setup
│   └── LINKEDIN_SEARCH_FIX.md         # LinkedIn search troubleshooting
│
└── Subdirectories/
    ├── OpenAI Chatbot/                # Alternative location
    └── Ollama Chatbot/                # Alternative location
```

---

## 🔧 Technical Details

### Architecture

```
User Input
    ↓
Streamlit UI
    ↓
LangChain Chain
    ↓
LLM Provider (OpenAI/Ollama)
    ↓
Response Processing
    ↓
Display Results
```

### Key Components

#### 1. **LangChain Integration**
- Uses LangChain for LLM abstraction
- Consistent interface across providers
- Easy to switch between models

#### 2. **Session State Management**
- Chat history stored in `st.session_state`
- Conversation threads managed separately
- Persistent during session

#### 3. **Web Search & Scraping**
- **SerpAPI**: For accurate Google search (optional)
- **DuckDuckGo**: Free alternative (fallback)
- **BeautifulSoup**: Web scraping engine
- **Agent-based**: AI decides when to search

#### 4. **Model Detection**
- **OpenAI**: Automatic model availability check
- **Ollama**: API call to list installed models

### Technology Stack

- **Streamlit**: Web framework
- **LangChain**: LLM orchestration
- **OpenAI API**: Cloud LLM provider
- **Ollama**: Local LLM provider
- **BeautifulSoup**: Web scraping
- **DuckDuckGo/SerpAPI**: Web search

---

## ⚙️ Configuration

### Environment Variables

#### Required
```bash
OPENAI_API_KEY=sk-...  # For OpenAI chatbot
```

#### Optional
```bash
LANGCHAIN_API_KEY=lsv2_...  # For LangSmith tracking
SERPAPI_API_KEY=...         # For better Google search
OLLAMA_BASE_URL=http://localhost:11434  # Custom Ollama URL
```

### Model Configuration

#### OpenAI Models
- **gpt-4o**: Most capable, recommended
- **gpt-4-turbo**: Fast and capable
- **gpt-4**: Standard GPT-4
- **gpt-3.5-turbo**: Fast and cost-effective

#### Ollama Models
- **mistral:latest**: Excellent balance
- **llama3.2:latest**: Latest Llama model
- **llama3.1:latest**: Stable Llama version
- **gemma:2b**: Fast, smaller model

### Response Parameters

- **Temperature**: 0.0 (focused) to 1.0 (creative)
- **Max Tokens**: Response length limit
- **Context Window**: Last 10 messages for context

---

## 🎯 Use Cases

### 1. **General Q&A**
- Ask questions on any topic
- Get AI-powered responses
- Maintain conversation context

### 2. **Web Research**
- Search for current information
- Scrape website content
- Find LinkedIn profiles
- Research topics from multiple sources

### 3. **Local Development**
- Use Ollama for offline development
- No API costs
- Privacy-focused
- Test different models

### 4. **Learning & Experimentation**
- Compare different models
- Test prompt engineering
- Learn LLM capabilities
- Experiment with parameters

---

## 🐛 Troubleshooting

### Common Issues

#### 1. **"No module named 'openai'"**
```bash
pip install openai
```

#### 2. **"Ollama not available"**
- Check Ollama is running: `ollama serve`
- Verify connection: `curl http://localhost:11434/api/tags`
- Check firewall settings

#### 3. **"No models available" (Ollama)**
```bash
ollama pull mistral
ollama list  # Verify models
```

#### 4. **"API key not found"**
- Create `.env` file
- Add `OPENAI_API_KEY=your_key`
- Restart the app

#### 5. **"Web search not working"**
- Check internet connection
- Verify SerpAPI key (if using)
- Try DuckDuckGo (free alternative)

#### 6. **"Chat history not persisting"**
- History is session-based (clears on refresh)
- This is expected behavior
- Use "Clear Chat History" to reset

### Getting Help

1. Check error messages in the UI
2. Review documentation files
3. Verify API keys and connections
4. Check model availability

---

## 📚 Documentation Files

- **`OpenAIChatbot_EXPLAINED.md`**: Line-by-line code explanation
- **`ENHANCEMENTS_GUIDE.md`**: Chat history and threads guide
- **`WEB_FEATURES_GUIDE.md`**: Web search and scraping guide
- **`OLLAMA_CHATBOT_GUIDE.md`**: Ollama chatbot usage
- **`QUICK_SETUP_WEB.md`**: Quick web setup guide
- **`LINKEDIN_SEARCH_FIX.md`**: LinkedIn search troubleshooting

---

## 🔄 Comparison: Chatbots

| Feature | OpenAI Basic | OpenAI Enhanced | Ollama Basic | Ollama Enhanced |
|---------|-------------|-----------------|--------------|-----------------|
| **Web Search** | ❌ | ✅ | ❌ | ❌ |
| **Web Scraping** | ❌ | ✅ | ❌ | ❌ |
| **Chat History** | ❌ | ✅ | ❌ | ✅ |
| **Conversation Threads** | ❌ | ✅ | ❌ | ❌ |
| **Model Detection** | ❌ | ❌ | ❌ | ✅ |
| **Ask Button** | ❌ | ✅ | ❌ | ✅ |
| **Context-Aware** | ❌ | ✅ | ❌ | ✅ |

---

## 🎓 Learning Resources

### Understanding the Code

1. **Start with**: `OpenAIChatbot_EXPLAINED.md`
   - Line-by-line explanations
   - Alternative approaches
   - Best practices

2. **Learn LangChain**:
   - Prompt templates
   - Chains and agents
   - Tool integration

3. **Explore Features**:
   - Web search implementation
   - Chat history management
   - Model detection

### Key Concepts

- **LangChain Chains**: `prompt | llm | parser`
- **Session State**: `st.session_state` for persistence
- **Agents**: Tool-using AI systems
- **Streamlit Widgets**: Interactive UI components

---

## 🚀 Advanced Usage

### Custom Prompts

Modify the prompt template in the code:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Your custom system message"),
    ("user", "Question: {question}")
])
```

### Adding New Tools

For web-enabled chatbot:

```python
new_tool = Tool(
    name="my_tool",
    func=my_function,
    description="What my tool does"
)
tools.append(new_tool)
```

### Custom Model Configuration

```python
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    max_tokens=2000,
    api_key=api_key
)
```

---

## 🔒 Security & Privacy

### API Keys
- Store in `.env` file (not in code)
- Never commit `.env` to Git
- Use different keys for dev/prod

### Data Privacy
- **OpenAI**: Data sent to OpenAI servers
- **Ollama**: All processing local (private)
- **Web Search**: Queries sent to search engines

### Recommendations
- Use Ollama for sensitive data
- Review OpenAI data usage policy
- Be aware of web search privacy

---

## 📊 Performance

### Response Times

- **OpenAI (Cloud)**: 1-5 seconds
- **Ollama (Local)**: 2-10 seconds (depends on model/hardware)
- **With Web Search**: +2-5 seconds

### Resource Usage

- **OpenAI**: No local resources
- **Ollama**: CPU/GPU intensive (depends on model)
- **Memory**: Varies by model size

---

## 🔮 Future Enhancements

Potential additions:
- [ ] Voice input/output
- [ ] Image generation support
- [ ] File upload and analysis
- [ ] Export chat history
- [ ] Multi-language support
- [ ] Custom model fine-tuning
- [ ] Plugin system
- [ ] API endpoints
- [ ] Database persistence
- [ ] User authentication

---

## 🤝 Contributing

Contributions welcome! Areas for contribution:

1. **New Features**: Add capabilities
2. **Bug Fixes**: Improve stability
3. **Documentation**: Enhance guides
4. **UI Improvements**: Better UX
5. **Performance**: Optimize code

---

## 📄 License

This project is open source and available for educational and commercial use.

---

## 🙏 Acknowledgments

- **OpenAI** for GPT models
- **Ollama** for local LLM infrastructure
- **LangChain** for LLM orchestration
- **Streamlit** for web framework
- **Community** for inspiration and support

---

## 📞 Support

For issues or questions:

1. Check documentation files
2. Review troubleshooting section
3. Check error messages in UI
4. Verify configuration

---

## 🎯 Quick Reference

### Start OpenAI Chatbot
```bash
streamlit run OpenAIChatbot_WEB_ENABLED.py
```

### Start Ollama Chatbot
```bash
ollama serve  # In separate terminal
streamlit run OllamaChatbot_ENHANCED.py
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Check Ollama Models
```bash
ollama list
```

### Pull New Model
```bash
ollama pull mistral
```

---

## 📈 Project Statistics

- **Total Chatbots**: 4 (2 basic, 2 enhanced)
- **LLM Providers**: 2 (OpenAI, Ollama)
- **Supported Models**: 10+ (across providers)
- **Features**: 15+ advanced features
- **Documentation**: 6 comprehensive guides

---

## 🎓 Best Practices

1. **Use Enhanced Versions**: More features, better UX
2. **Enable Web Tools**: For current information
3. **Use Ollama Locally**: For privacy-sensitive tasks
4. **Manage API Keys**: Store securely in `.env`
5. **Clear History**: When switching topics
6. **Monitor Usage**: Track API costs (OpenAI)
7. **Test Models**: Compare responses

---

## 📝 Example Queries

### General Questions
- "What is machine learning?"
- "Explain quantum computing"
- "How does neural networks work?"

### Web-Enabled Queries
- "What's the latest news about AI?"
- "Find information about Python 3.12"
- "Search for best practices in software development"

### Research Queries
- "Research the impact of AI on healthcare"
- "Find recent developments in quantum computing"
- "Look up information about [topic]"

---

**Built with ❤️ for making AI accessible to everyone!**

---

## 🚀 Get Started Now!

```bash
# 1. Activate virtual environment
source .venv/bin/activate

# 2. Set up .env file
echo "OPENAI_API_KEY=your_key" > .env

# 3. Run your preferred chatbot
streamlit run OpenAIChatbot_WEB_ENABLED.py
# or
streamlit run OllamaChatbot_ENHANCED.py
```

**Happy Chatting! 🎉**

