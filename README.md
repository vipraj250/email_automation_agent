# Local Gmail AI Reply Agent

A Python project that uses the Gmail API and a local Ollama model to generate and send short email replies. It checks unread inbox messages, applies sender and automated-email filters, and records handled message IDs to reduce duplicate replies.

## How it works

1. Connects to Gmail using OAuth.
2. Finds unread inbox messages.
3. Skips senders not listed in the private allowlist and messages detected as automated or bulk.
4. Uses the local Gemma 3 model to generate a brief reply.
5. Sends the reply in the original email thread and records the message ID.

## Technology

- Python
- Gmail API
- Ollama with `gemma3:4b`
- LangChain Ollama integration

## Setup on Windows

1. Install Python and [Ollama](https://ollama.com/).
2. Download the model:

   ```powershell
   ollama pull gemma3:4b
3. In the project folder, create and activate a virtual environment, then install the packages:
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
4. In Google Cloud, enable the Gmail API and create OAuth credentials for a desktop application. Save the downloaded file as credentials.json in the project folder.

5. Copy local_settings.example.py to local_settings.py. Put the exact email addresses you trust in ALLOWED_SENDERS in local_settings.py.

6. Make sure credentials.json, token.json, and local_settings.py are not committed to GitHub.

7. Test with a dedicated account and a message you control:
   python gmail_test.py
Automatic scheduling
On Windows, Task Scheduler can run the script periodically while the user is logged in. Keep the computer on and connected to the internet for scheduled runs.
Safety
This script sends real email replies. Start with a test account and a narrow allowlist. Review the allowlist before enabling automatic scheduling. Model-generated replies can be inaccurate, so use this project only with senders and messages for which automatic replies are appropriate.
OAuth credentials, access tokens, the private sender list, and processed message IDs belong in local files and should not be published.

 