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
