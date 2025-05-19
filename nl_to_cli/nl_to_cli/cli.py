import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from .agents import (
    InputHandlerAgent,
    CommandTranslatorAgent,
    CLIExecutorAgent,
    LoggerAgent
)

app = typer.Typer()
console = Console()

def process_command(command: str, input_handler: InputHandlerAgent, translator: CommandTranslatorAgent, 
                   executor: CLIExecutorAgent, logger: LoggerAgent) -> None:
    """
    Process a single command through the agent pipeline.
    """
    try:
        # Process input
        console.print(Panel("Processing input...", title="Step 1: Input Processing"))
        input_data = input_handler.process_input(command)

        # Translate command
        console.print(Panel("Translating to CLI command...", title="Step 2: Command Translation"))
        cli_command = translator.translate_command(input_data)
        console.print(f"[bold blue]Translated command:[/] {cli_command}")

        # Execute command
        console.print(Panel("Executing command...", title="Step 3: Command Execution"))
        result = executor.execute_command(cli_command)

        # Log execution
        console.print(Panel("Logging execution...", title="Step 4: Logging"))
        logger.log_execution(input_data, result)

        # Display results
        if result.success:
            console.print(Panel(result.output, title="Command Output", border_style="green"))
            # If the command was a Wikipedia search and saved to a file, display the file contents
            if (
                command.lower().startswith("search the web for") and
                "save" in command.lower()
            ):
                try:
                    output_file = command.lower().split("save")[-1].strip().split()[-1]
                    if output_file:
                        with open(output_file, "r") as f:
                            file_content = f.read()
                        console.print(Panel(file_content, title=f"Contents of {output_file}", border_style="cyan"))
                except Exception as e:
                    console.print(Panel(f"Could not read {output_file}: {e}", border_style="red"))
        else:
            console.print(Panel(
                f"Error: {result.error}\nOutput: {result.output}",
                title="Command Failed",
                border_style="red"
            ))

    except Exception as e:
        console.print(Panel(
            str(e),
            title="Error",
            border_style="red"
        ))
        raise typer.Exit(1)

@app.command()
def execute_command(
    command: str = typer.Argument(None, help="The natural language command to execute")
):
    """
    Execute natural language commands interactively or from command line.
    If no command is provided, enters interactive mode.
    """
    # Initialize agents
    input_handler = InputHandlerAgent()
    translator = CommandTranslatorAgent()
    executor = CLIExecutorAgent()
    logger = LoggerAgent()

    if command:
        # Single command mode
        process_command(command, input_handler, translator, executor, logger)
    else:
        # Interactive mode
        console.print(Panel(
            "Welcome to NL-to-CLI interactive mode!\n"
            "Type your natural language commands and press Enter to execute.\n"
            "Type 'exit' or 'quit' to end the session.",
            title="Interactive Mode",
            border_style="blue"
        ))
        
        while True:
            try:
                command = Prompt.ask("\nEnter your command")
                if command.lower() in ['exit', 'quit']:
                    console.print("[yellow]Goodbye![/]")
                    break
                
                process_command(command, input_handler, translator, executor, logger)
                
            except KeyboardInterrupt:
                console.print("\n[yellow]Session terminated by user.[/]")
                break
            except Exception as e:
                console.print(Panel(
                    str(e),
                    title="Error",
                    border_style="red"
                ))

if __name__ == "__main__":
    app() 