# NL-to-CLI Super Agent

A powerful automation system that translates natural language instructions into CLI commands using Gemini 2.0 Flash and CrewAI.

## Features

- Natural language to CLI command translation
- Secure command execution
- Comprehensive logging and error tracking
- Clean output formatting

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the agent with a natural language command:

```bash
python main.py "your natural language command here"
```

## Architecture

The system consists of four main agents:

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