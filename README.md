# Coursera-MLOps-C2-Final-HuggingFace

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers-yellow)](https://huggingface.co/)
[![Gradio](https://img.shields.io/badge/Gradio-4.31.0-orange.svg)](https://gradio.app/)
[![Click](https://img.shields.io/badge/Click-8.1.7-green.svg)](https://click.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)

This repository contains the final laboratory assignment for the MLOps course, focusing on the development of web applications using **Hugging Face** and **Gradio**, alongside the implementation of a Command-Line Interface (CLI) using the **Click** framework.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Dependency Modernization and Python 3.12 Compatibility](#dependency-modernization-and-python-312-compatibility)
4. [Completed Tasks](#completed-tasks)
   - [Task A: Gradio Calculator Application](#task-a-gradio-calculator-application)
   - [Task B: Summarization Application](#task-b-summarization-application)
   - [Task C: Model Customization](#task-c-model-customization)
   - [Task D: Command-Line Interface (CLI)](#task-d-command-line-interface-cli)
5. [Reflections](#reflections)
6. [Origin and Attribution](#origin-and-attribution)
7. [License](#license)
8. [Author](#author)

## Project Structure

    .
    ├── helloApp.py              # Task A: Gradio-based Calculator Application
    ├── summarizeApp.py          # Task B: Gradio-based Summarization Application
    ├── load_model.py            # Task C: Programmatic Model Loading and Customization
    ├── cli_summarize.py         # Task D: Command-Line Interface using Click
    ├── summarizeApp/            # Locally cached DistilBART model directory
    ├── text.txt                 # Sample text for summarization tasks
    ├── requirements.txt         # Python 3.12 project dependencies
    ├── REFLECTIONS.md           # Academic responses to laboratory reflection questions
    └── README.md                # Project documentation (this file)

## Prerequisites

- Python 3.12
- Virtual environment (`.venv`)
- Installation of required dependencies:

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt

## Dependency Modernization and Python 3.12 Compatibility

The original `requirements.txt` provided in the upstream repository was designed for legacy Python versions (circa 2022, Python 3.8/3.9). To ensure compatibility with the modern **Python 3.12.1** environment used in this laboratory, a comprehensive modernization of the dependency stack was performed. This engineering effort involved resolving several critical conflicts:

1.  **Removal of `pkg_resources` (Python 3.12)**: Legacy `pandas==1.5.0` failed to build from source because Python 3.12's `setuptools` ecosystem removed the deprecated `pkg_resources` module. This was resolved by upgrading to `pandas==2.2.2`, which provides pre-compiled wheels for Python 3.12.
2.  **Dependency Conflict Resolution**: `databricks-sql-connector==3.1.0` strictly required `pandas<2.2.0`, conflicting with the required Python 3.12 upgrades. This was resolved by upgrading to `databricks-sql-connector==4.0.3`, which supports `pandas<4.0.0`.
3.  **Deep Learning and ML Ecosystem**: `torch`, `tensorflow`, and `transformers` were updated to versions with official Python 3.12 support (`torch==2.2.2`, `tensorflow==2.16.1`, `transformers==4.40.2`). 
4.  **Web Frameworks**: `gradio==3.4.1` lacks Python 3.12 compatibility; thus, it was upgraded to `gradio==4.31.0`.

This modernization ensures that the laboratory can be executed reproducibly in modern cloud environments (such as GitHub Codespaces) without compilation errors.

## Completed Tasks

### ✅ Task A: Gradio Calculator Application

`helloApp.py` implements a web-based calculator that computes the sum of two numbers utilizing the `mylib.calculator.add` function.

    python helloApp.py

Upon execution, the Gradio interface is accessible via the provided local URL (or via port forwarding in VS Code).

### ✅ Task B: Summarization Application

`summarizeApp.py` loads the `sshleifer/distilbart-cnn-12-6` model and provides a Gradio interface for text summarization.

    python summarizeApp.py

Users can input excerpts from `text.txt` to observe the generated summaries.

### ✅ Task C: Model Customization

`load_model.py` illustrates the methodology for loading the summarization model from the local `summarizeApp/` directory and applying it to an external file (`input.txt`).

    cp text.txt input.txt
    python load_model.py

### ✅ Task D: Command-Line Interface (CLI)

`cli_summarize.py` provides a CLI implementation that replicates the summarization functionality for automated workflows.

    python cli_summarize.py --archivo text.txt
    python cli_summarize.py --texto "Artificial intelligence is transforming the industry."

## Reflections

For detailed academic responses to the laboratory reflection questions, please refer to [REFLECTIONS.md](REFLECTIONS.md).

## Origin and Attribution

This project is a fork of the original educational repository [nogibjj/Coursera-MLOps-C2-Final-HuggingFace](https://github.com/nogibjj/Coursera-MLOps-C2-Final-HuggingFace), created by Noah Gift for the MLOps Specialization on Coursera. The modifications and extensions presented herein (Tasks A through D, alongside the Python 3.12 dependency modernization) were developed by the author of this fork.

## License

This project is licensed under the **MIT License**, inherited directly from the original upstream repository. See the `LICENSE` file (if applicable) or the [Open Source Initiative](https://opensource.org/licenses/MIT) for more details.

## Author

Antonio Bernal Navarro