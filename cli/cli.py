import argparse
from cli.commands.agent_commands import AgentCommands
from cli.commands.prompt_commands import PromptCommands
from cli.commands.tool_commands import ToolCommands

def main():
    parser = argparse.ArgumentParser(description="Agent Lambda CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Agent commands
    agent_parser = subparsers.add_parser("agent", help="Agent-related commands")
    agent_parser.add_argument("action", choices=["create", "respond", "list"], help="Action to perform")
    agent_parser.add_argument("--name", help="Name of the agent")
    agent_parser.add_argument("--message", help="Message to send to the agent")

    # Prompt commands
    prompt_parser = subparsers.add_parser("prompt", help="Prompt-related commands")
    prompt_parser.add_argument("action", choices=["list", "add", "remove"], help="Action to perform")
    prompt_parser.add_argument("--name", help="Name of the prompt")
    prompt_parser.add_argument("--text", help="Prompt text")

    # Tool commands
    tool_parser = subparsers.add_parser("tool", help="Tool-related commands")
    tool_parser.add_argument("action", choices=["list", "execute"], help="Action to perform")
    tool_parser.add_argument("--name", help="Name of the tool")
    tool_parser.add_argument("--args", nargs="+", help="Arguments for the tool")

    args = parser.parse_args()

    if args.command == "agent":
        AgentCommands.execute(args)
    elif args.command == "prompt":
        PromptCommands.execute(args)
    elif args.command == "tool":
        ToolCommands.execute(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
