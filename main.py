import typer
from rich.console import Console
from rich.panel import Panel
from agents import (
    InputHandlerAgent,
    CommandTranslatorAgent,
    CLIExecutorAgent,
    LoggerAgent
)

app = typer.Typer()
console = Console()

@app.command()
def execute_command(command: str):
    """
    Execute a natural language command by converting it to CLI and running it.
    """
    try:
        # Initialize agents
        input_handler = InputHandlerAgent()
        translator = CommandTranslatorAgent()
        executor = CLIExecutorAgent()
        logger = LoggerAgent()

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

if __name__ == "__main__":
    app() 