import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import argparse
from agent.agent import Agent
from llm_wrappers.openai_llm import OpenAILLM
from tools.file_operation_tool import FileOperationTool
from llm_wrappers.mock_llm import MockLLM
from llm_wrappers.google_gemini import GoogleGeminiLLM
from llm_wrappers.ollama import OllamaLLM
from tools.search_tool import SearchTool

def get_llm(provider, api_key):
    if provider == "openai":
        return OpenAILLM(api_key)
    elif provider == "google_gemini":
        return GoogleGeminiLLM(api_key)
    elif provider == "ollama":
        return OllamaLLM(api_key)
    elif provider == "mock":
        return MockLLM()
    else:
        raise ValueError("Unsupported LLM provider. Choose from 'openai', 'google_gemini', or 'ollama'.")
    
def main():
    parser = argparse.ArgumentParser(description="AI Agent Framework CLI")
    parser.add_argument('--goal', type=str, required=True, help="Goal for the agent")
    parser.add_argument('--tasks', nargs='+', help="List of tasks for the agent")
    parser.add_argument('--llm_provider', type=str, required=True, choices=['openai', 'google_gemini', 'ollama', 'mock'], help="Choose the LLM provider.")
    parser.add_argument('--api_key', type=str, required=True, help="API key for the selected LLM provider.")
    
    args = parser.parse_args()
    tasks = []
    for task_str in args.tasks:
        if task_str.startswith('search:'):
            query = task_str.split('query=')[1]
            tasks.append({'tool': 'SearchTool', 'parameters': {'query': query}})
        elif task_str.startswith('file:'):
            # Example: file:action=read,file_path=test.txt
            params = dict(param.split('=') for param in task_str[5:].split(','))
            tasks.append({'tool': 'FileOperationTool', 'parameters': params})
    
    # Initialize components
    llm = get_llm(args.llm_provider, args.api_key)
    tools = [SearchTool(), FileOperationTool()]
    agent = Agent(goal=args.goal, llm=llm, tools=tools)
    
    # Set up and execute agent tasks
    agent.initialize_agent(tasks)
    while agent.state_manager.get_current_state() != 'Completed':
        agent.execute_task()

if __name__ == "__main__":
    main()
