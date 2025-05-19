from typing import Optional, Dict, Any
from crewai import Agent
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.logging import RichHandler
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger("nl-to-cli")

# Initialize Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

class CommandInput(BaseModel):
    command: str
    environment_details: Optional[Dict[str, Any]] = None

class CommandOutput(BaseModel):
    success: bool
    output: str
    error: Optional[str] = None

class InputHandlerAgent:
    def __init__(self):
        self.agent = Agent(
            role="Input Handler",
            goal="Process and validate user input",
            backstory="Expert at processing and validating natural language commands",
            verbose=True
        )

    def process_input(self, command: str) -> CommandInput:
        # Basic input sanitization
        command = command.strip()
        if not command:
            raise ValueError("Command cannot be empty")
        
        return CommandInput(command=command)

class CommandTranslatorAgent:
    def __init__(self):
        self.agent = Agent(
            role="Command Translator",
            goal="Convert natural language to CLI commands",
            backstory="Expert at translating natural language to precise CLI commands",
            verbose=True
        )

    def translate_command(self, input_data: CommandInput) -> str:
        prompt = f"""
        Translate the following natural language command into a CLI command:
        Command: {input_data.command}
        
        Environment details: {input_data.environment_details}
        
        Return ONLY the CLI command, nothing else.
        """
        
        response = model.generate_content(prompt)
        return response.text.strip()

class CLIExecutorAgent:
    def __init__(self):
        self.agent = Agent(
            role="CLI Executor",
            goal="Execute CLI commands securely",
            backstory="Expert at executing CLI commands safely and efficiently",
            verbose=True
        )
        self.console = Console()

    def execute_command(self, command: str) -> CommandOutput:
        try:
            # Execute command and capture output
            import subprocess
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            
            return CommandOutput(
                success=result.returncode == 0,
                output=result.stdout,
                error=result.stderr if result.returncode != 0 else None
            )
        except Exception as e:
            return CommandOutput(
                success=False,
                output="",
                error=str(e)
            )

class LoggerAgent:
    def __init__(self):
        self.agent = Agent(
            role="Logger",
            goal="Track and log execution details",
            backstory="Expert at logging and tracking command execution details",
            verbose=True
        )

    def log_execution(self, input_data: CommandInput, output: CommandOutput):
        log_entry = {
            "input_command": input_data.command,
            "success": output.success,
            "output": output.output,
            "error": output.error
        }
        
        logger.info(f"Command Execution Log: {log_entry}")
        return log_entry 