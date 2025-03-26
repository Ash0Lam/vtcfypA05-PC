import os
from dotenv import load_dotenv

# Load environment variables from .env file (if exists)
load_dotenv()

# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "your_azure_openai_api_key_here")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "your_azure_openai_endpoint_here")
AZURE_SPEECH_API_KEY = os.getenv("AZURE_SPEECH_API_KEY", "your_azure_speech_api_key_here")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION", "your_azure_speech_region_here")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-35-turbo")

# SerpApi Configuration
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "your_serpapi_api_key_here")

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "your_telegram_bot_token_here")

# Google Custom Search Engine Configuration
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID", "your_google_cse_id_here")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "your_google_api_key_here")