# Auto-Message-Sender

A Flask-based desktop automation tool that sends WhatsApp messages via WhatsApp Web and auto-types into any active input field using PyAutoGUI.

## Features

- Schedule WhatsApp messages to send at a specific time
- Auto-type messages into any input box on your screen
- Control repeat count and interval between messages

## Installation

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Usage

**WhatsApp Sender** — Schedule messages to be sent via WhatsApp Web. Make sure WhatsApp Web is open and logged in before the scheduled time.

**Everywhere Sender** — Click into any input field, then trigger the tool to auto-type your message instantly.

## Requirements

- Python 3.8+
- WhatsApp Web open in browser (for WhatsApp Sender)

## Tech Stack

- [Flask](https://flask.palletsprojects.com/) — web interface
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — keyboard automation
- [pywhatkit](https://pypi.org/project/pywhatkit/) — WhatsApp message scheduling
- HTML/CSS — frontend designed with AI assistance