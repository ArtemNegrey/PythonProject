# API and UI Testing Project

This project contains automated tests for verifying a REST API (using the `requests` library) and a user interface (using `Playwright` and `pytest`).

## Project Structure
* `tests/api/` — API tests for the reqres.in endpoint (includes GET, POST, PUT, and DELETE methods).
* `tests/ui/` — UI tests for verifying the login form on the-internet.herokuapp.com.
* `conftest.py` — Shared fixtures, including API session setup with an API key and browser setup/teardown.

## Setup Instructions

1. **Clone the repository and navigate to the project folder:**
   ```bash
   git clone [https://github.com/ArtemNegrey/PythonProject](https://github.com/ArtemNegrey/PythonProject)
   cd PythonProject
2. **Create and activate a virtual environment for macOS/Linux:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
3. **Create and activate a virtual environment for Windows:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
4. **Install dependencies:**
    ```bash
   pip install -r requirements.txt
5. **Install browsers for Playwright:**
    ```bash
   playwright install chromium
## Run instructions
1. **Run only API tests (with the -s flag to display setup/teardown logs from fixtures):**
    ```bash
   pytest -s tests/api
2. **Run only UI tests:**
    ```bash
   pytest tests/ui
3. **Run all tests:**
    ```bash
   pytest