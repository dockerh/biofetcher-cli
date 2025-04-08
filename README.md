# Biofetcher CLI

## Overview
`biofetcher-cli` is a Python-based Command Line Interface (CLI) tool that downloads biomedical data files from the web. It supports both synchronous and asynchronous file download methods, providing flexible options for handling large datasets.

## Features
- Command-line interface development with `argparse`
- Asynchronous and synchronous downloading via `aiohttp` and `requests`
- Modular Python structure for future extensibility (e.g., Globus integration)
- Unit testing using `pytest` and `pytest-asyncio`
- **Sync Download**: Downloads files using synchronous requests.
- **Async Download**: Downloads files asynchronously, optimizing performance for large datasets.
- Supports **output file naming** for easy file management.

## Installation
To use `biofetcher-cli`, you need Python 3.7+ and pip. Install the dependencies with:

```bash
pip install -r requirements.txt
