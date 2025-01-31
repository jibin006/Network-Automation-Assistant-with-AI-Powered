#Network Automation Assistant with AI-Powered Insights 

from netmiko import ConnectHandler
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import argparse
import warnings
from cryptography.utils import CryptographyDeprecationWarning

warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)

load_dotenv(dotenv_path=".env")
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

def execute_network_command(command):
    """Execute commands on Cisco device using Netmiko"""
    command = command.strip("'\"")
    
    device = {
        'device_type': 'cisco_ios',
        'host': 'sandbox-iosxr-1.cisco.com',
        'username': 'admin',
        'password': 'C1sco12345',
        'port': 22,
    }
    
    try:
        with ConnectHandler(**device) as net_connect:
            output = net_connect.send_command(command)
            if "Invalid input" in output or "% Error" in output:
                return f"Error executing command: {output}"
            return output
    except Exception as e:
        return f"Error executing command: {str(e)}"

def create_ai_assistant():
    """Create an AI assistant for answering questions"""
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.1
    )
    return llm

def ask_ai_about_output(llm, command_output, question):
    """Ask AI about the command output"""
    prompt = f"""
    Here is the output of a network command:
    {command_output}
    
    Question about this output: {question}
    
    Please provide a clear, concise answer focusing specifically on the question asked.
    """
    
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error getting AI response: {str(e)}"

def interactive_mode(command_output):
    """Enter interactive mode to ask questions about the output"""
    llm = create_ai_assistant()
    
    print("\n=== Interactive Mode ===")
    print("You can ask questions about the output (type 'exit' to quit)")
    
    while True:
        question = input("\nYour question: ").strip()
        
        if question.lower() in ['exit', 'quit', 'q']:
            print("Exiting interactive mode...")
            break
            
        if question:
            print("\nAI Response:")
            response = ask_ai_about_output(llm, command_output, question)
            print(response)

def main():
    parser = argparse.ArgumentParser(description='Network Automation Assistant')
    parser.add_argument('-q', '--query', type=str, required=True, help='Enter your network command query')
    args = parser.parse_args()

    print("\n=== Network Automation Assistant ===")
    print(f"Processing query: {args.query}\n")
    
    # Execute command and store output
    command_output = execute_network_command(args.query)
    print(command_output)
    
    # Enter interactive mode
    interactive_mode(command_output)

if __name__ == "__main__":
    main()
