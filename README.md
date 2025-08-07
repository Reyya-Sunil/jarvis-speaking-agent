# 🤖 Jarvis - AI Speaking Agent by Sunil

Jarvis is a voice-interactive AI agent built by **Sunil**. It listens, understands, speaks, and performs actions like opening YouTube or shutting down your PC—all with natural conversation powered by AI. Now compatible with **DeepSeek** for local or private language model inference.

---

## ✨ Features

- 🎙️ **Voice Recognition**: Converts speech to text using your microphone
- 🧠 **AI-Powered Conversations**:
  - Supports **OpenAI GPT models**
  - Supports **DeepSeek** (open-source LLM)
- 🔊 **Text-to-Speech**: Uses natural-sounding voice synthesis
- 🖥️ **System Control**:
  - 🔌 Shut down your PC via voice
  - 📺 Open YouTube on command
- 💬 **Custom Wake Word** *(optional)*
- 🌐 **Internet-Connected Info Fetching** *(optional)*

---

## 🧠 Model Options

| Model Engine  | Description                           |
|---------------|---------------------------------------|
| OpenAI GPT    | Cloud-based language model (API key required) |
| DeepSeek      | Local or server-hosted LLM (no API key required) |

You can configure Jarvis to use either model depending on your setup.

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Microphone access
- For OpenAI:
  - [OpenAI API Key](https://platform.openai.com/)
- For DeepSeek:
  - Install `transformers`, `torch`, and load DeepSeek model

### Clone and Install


git clone https://github.com/your-username/jarvis-ai-agent.git
cd jarvis-ai-agent
pip install -r requirements.txt


---



