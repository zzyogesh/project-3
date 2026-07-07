
# Credit Card Web App

Simple Flask web app for running credit-card-related predictions using a trained model.

## Overview

This repository contains a minimal Flask application (`app.py`) that loads a trained model from the `model/` directory and exposes a web UI under `templates/` to submit inputs and view results.

## Features

- Web frontend for entering data and viewing prediction results
- Loads a persisted ML model from `model/`
- Lightweight single-file Flask app for demonstration and testing

## Requirements

- Python 3.8+ (3.10 recommended)
- Dependencies listed in `requirements.txt` (if present). Common packages include `flask`, `pandas`, and the ML libraries used to train the model (e.g. `scikit-learn`).

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # macOS / Linux
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

If no `requirements.txt` exists, install `flask` and any ML packages your model requires.

## Run

Start the app either by running `app.py` directly or via Flask:

```bash
python app.py
# or
set FLASK_APP=app.py
flask run
```

Then open a browser to `http://127.0.0.1:5000/` to use the UI.

## Usage

- Use the main page (`templates/index.html`) to enter the input values required by the model.
- Submit the form to see prediction results rendered by `templates/result.html`.

## File structure

- `app.py` — Flask application entrypoint
- `model/` — persisted trained model and related artifacts
- `templates/` — HTML templates (`index.html`, `result.html`)
- `static/` — static assets such as `style.css`
- `README.MD` — this file

## Notes

- Ensure the model file name and loading code in `app.py` match the files in `model/`.
- If you want, I can add a `requirements.txt` and a small `Procfile` for deployment.

## License

This project is provided as-is. Add a license if you plan to publish it.
