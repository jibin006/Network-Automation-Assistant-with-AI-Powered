# 🤖 Network Automation Assistant with AI-Powered Insights

## Overview

This Network Automation Assistant is an innovative Python tool that combines network management capabilities with AI-powered insights, revolutionizing how network administrators troubleshoot and interact with network devices.

## 🌟 Key Features

- **Automated Cisco IOS Configuration**: Seamlessly execute network commands using Netmiko
- **AI-Powered Insights**: Leverage Google's Gemini Pro AI through LangChain for intelligent analysis
- **Interactive CLI**: Real-time troubleshooting with AI-assisted interpretation

## 🛠 Prerequisites

Before you begin, ensure you have the following:

- Python 3.8+
- Cisco network device access
- Google AI API Key

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-automation-assistant.git
   cd network-automation-assistant
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Google API Key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## 🚀 Usage

### Running the Assistant

Execute network commands with AI-powered insights:

```bash
python network_assistant.py -q "show interfaces"
```

### Interactive Mode

After running a command, you'll enter an interactive mode where you can:
- Ask questions about the command output
- Get AI-generated insights
- Troubleshoot network issues in real-time

### Example Workflow

1. Check interface status:
   ```bash
   python network_assistant.py -q "show interfaces"
   ```

2. Ask follow-up questions:
   - "Are there any interface errors?"
   - "What might be causing this performance issue?"

## 🔒 Security Considerations

- Use strong, unique credentials
- Never commit sensitive information to version control
- Regularly rotate API keys and credentials

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Requirements File (requirements.txt)

```
netmiko==4.1.2
langchain==0.1.0
google-generativeai==0.3.1
python-dotenv==1.0.0
cryptography==42.0.2
```

## ⚠️ Disclaimer

This tool is for educational and professional network management purposes. Always ensure proper authorization before accessing network devices.

## 📞 Support

For issues or questions, please open a GitHub issue or contact the repository maintainer.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Happy Network Automating! 🌐🤖**
