from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nl-to-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A natural language to CLI command translator using Gemini AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nl-to-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "crewai>=0.11.0",
        "google-generativeai>=0.3.0",
        "python-dotenv>=1.0.0",
        "rich>=13.7.0",
        "pydantic>=2.5.0",
        "typer>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "nl-to-cli=nl_to_cli.cli:app",
        ],
    },
) 