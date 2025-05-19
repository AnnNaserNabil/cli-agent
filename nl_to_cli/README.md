# NL-to-CLI

A powerful Python package that translates natural language instructions into CLI commands using Gemini AI and CrewAI.

## Features

- Natural language to CLI command translation
- Secure command execution
- Comprehensive logging and error tracking
- Clean output formatting
- Easy-to-use command-line interface

## Installation

```bash
pip install nl-to-cli
```

## Setup

1. Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.env` file in your project directory:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Command Line

```bash
nl-to-cli "your natural language command here"
```

Example:
```bash
nl-to-cli "list all files in the current directory"
```

### Python API

```python
from nl_to_cli import InputHandlerAgent, CommandTranslatorAgent, CLIExecutorAgent, LoggerAgent

# Initialize agents
input_handler = InputHandlerAgent()
translator = CommandTranslatorAgent()
executor = CLIExecutorAgent()
logger = LoggerAgent()

# Process command
input_data = input_handler.process_input("list all files")
cli_command = translator.translate_command(input_data)
result = executor.execute_command(cli_command)
logger.log_execution(input_data, result)
```

## Architecture

The package consists of four main agents:

1. **InputHandlerAgent**: Processes and validates user input
2. **CommandTranslatorAgent**: Converts natural language to CLI commands
3. **CLIExecutorAgent**: Executes commands securely
4. **LoggerAgent**: Tracks and logs execution details

## Security

- All CLI commands are executed in a controlled environment
- Input sanitization is performed before command translation
- Command execution is logged for audit purposes

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 