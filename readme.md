

---

# AI Chat - Powered by Groq and Langchain

**AI Chat** is an interactive AI chatbot application powered by **Groq** and **Langchain**. This app provides real-time, conversational AI that can respond to various queries related to **industrial coatings** and **corrosion protection**. The bot leverages a large language model (LLM) to deliver high-quality responses within a defined scope, creating a seamless experience for users.

## 🛠️ **Tech Stack**

- **Frontend**: [Streamlit](https://streamlit.io/) for building the web app.
- **Backend**: [Groq](https://groq.com/) for AI-powered conversation, using Langchain integration.
- **Langchain**: A framework for building applications with LLMs, enabling conversation memory, prompt templates, and more.
- **Memory Management**: [ConversationBufferWindowMemory](https://langchain.readthedocs.io/en/latest/modules/memory.html#conversationbuffwindowmemory) for maintaining context and chat history.
  
## 🎨 **Features**

- **Real-time Chat**: An interactive chat interface where users can converse with the AI in real time.
- **Custom Chatbot**: Specialized AI assistant for answering questions about **industrial coatings**, **corrosion protection**, and related fields.
- **Responsive UI**: A modern and minimalist UI with a dark theme for a sleek user experience.
- **Conversation History**: Memory to retain context across multiple messages.
- **AI-Assisted Answers**: The assistant only provides accurate, detailed responses within a specific domain (industrial coatings and corrosion protection).
- **Error Handling**: Graceful error handling for unexpected input or issues.

## 🚀 **Installation**

### Prerequisites

Before you can run this project, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/)
- [Groq API Key](https://groq.com/) (set up your API key in Streamlit secrets)

### Setup Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ai-chat.git
   cd ai-chat
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your **Groq API Key** in the Streamlit secrets:
   - Go to **.streamlit/secrets.toml** and add your **groq_api_key**:
     ```toml
     [groq]
     groq_api_key = "your-groq-api-key-here"
     ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

   This will open a local web page with the AI chatbot.

---

## 🎮 **How to Use**

- **Type your message** in the input box and hit Enter to send your query.
- The assistant will respond with detailed, accurate information about **industrial coatings** and **corrosion protection**.
- The chatbot only answers questions related to these topics. Any unrelated question will be politely declined.

---

## 🔗 **Live Demo**

You can try out the app live by visiting the following link:

🔗 **[Live Demo - AI Chat](https://maharshi-chatbot.streamlit.app/)**

---

## ⚙️ **Customization**

You can customize the following in the app:

- **System Prompt**: Modify the `system_prompt` variable to change the scope and behavior of the AI assistant. Currently, it’s focused on industrial coatings and corrosion protection.
- **UI Theme**: Modify the **CSS** styles in the `st.markdown()` section to change the appearance of the chat window, buttons, etc.

---

## 🔧 **Dependencies**

- **Streamlit**: For building the web app.
- **Groq**: For leveraging LLMs in a conversational setup.
- **Langchain**: For chaining language model prompts and maintaining conversation memory.
- **datetime**: For managing timestamps in messages.
- **time**: For adding delays to simulate AI thinking time.

You can check the dependencies listed in the `requirements.txt` file.

---

## 📜 **Future Features**

- Expand the knowledge base to support more industries.
- Add multi-language support for diverse users.
- Improve the user interface with more interactive elements.

---

## 💬 **Contact**

For more information or any queries, feel free to reach out:

- **Email**: [maharshi2406@gmail.com](mailto:maharshi2406@gmail.com)
- **LinkedIn**: [Maharshi Desai](https://www.linkedin.com/in/maharshi-desai-30143a279/)

---

