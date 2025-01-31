
# Network Automation Assistant with AI-Powered Insights 🤖

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent assistant combining network automation with AI analysis to simplify Cisco device management. Execute commands and get real-time AI insights through an interactive CLI.

## Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

## 🚀 Features
- **Automated Command Execution**: Directly run Cisco IOS commands using Netmiko
- **AI Analysis**: Google's Gemini Pro integration for output interpretation
- **Interactive Mode**: Chat-like interface for real-time troubleshooting
- **Sandbox Ready**: Pre-configured for Cisco DevNet sandbox (sandbox-iosxr-1.cisco.com)
- **Error Handling**: Automatic detection of common command errors

## 📋 Prerequisites
- Python 3.8 or newer
- Google API key ([Get API key](https://makersuite.google.com/app/apikey))
- SSH access to target network device

## 📥 Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/network-ai-assistant.git
cd network-ai-assistant
2. Create Virtual Environment
bash
Copy
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
3. Install Dependencies
bash
Copy
pip install -r requirements.txt
Create requirements.txt with:

Copy
langchain-google-genai
netmiko
python-dotenv
langchain
4. Configure Environment
Create .env file in project root:

bash
Copy
echo "GOOGLE_API_KEY=your_actual_api_key" > .env
🔧 Configuration
For Custom Devices
Modify device dictionary in execute_network_command():

python
Copy
device = {
    'device_type': 'cisco_ios',
    'host': 'your_device_ip',
    'username': 'your_username',
    'password': 'your_password',
    'port': 22,  # SSH port
}
AI Settings
Adjust in create_ai_assistant():

python
Copy
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.1  # Range: 0.0 (strict) to 1.0 (creative)
)
💻 Usage
Basic Command Execution
bash
Copy
python3 main.py -q "show interfaces"
Interactive AI Session
After command execution, ask questions like:

bash
Copy
"What does the output indicate about interface status?"
"Are there any error counters increasing?"
"Explain the MAC address table"
Type 'exit' to quit
Example Workflow
bash
Copy
# Check device version
python3 main.py -q "show version"

# During interactive mode:
Your question: "What's the device uptime?"
AI Response: The device has been up for 2 weeks, 3 days, 5 hours...

Your question: "Is this IOS version vulnerable to CVE-2023-20198?"
AI Response: This version (17.6.1a) has no known vulnerabilities...
🛠 Troubleshooting
Issue	Solution
API Key Not Found	Verify .env file exists in root directory
Connection Timeout	Check device IP/credentials and network connectivity
Command Errors	Validate Cisco IOS command syntax
Cryptography Warnings	Normal behavior - warnings are intentionally suppressed
🤝 Contributing
Fork the project

Create feature branch (git checkout -b feature/NewFeature)

Commit changes (git commit -m 'Add NewFeature')

Push to branch (git push origin feature/NewFeature)

Open a Pull Request

📜 License
Distributed under MIT License - see LICENSE file for details
