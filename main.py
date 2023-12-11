"""Main entry point for the OpenAI Chatbot."""

import os
import asyncio
from dotenv import load_dotenv
from api_service import OpenAIAPIService


async def main():
    """Main entry point for the OpenAI Chatbot."""

    print("Welcome to the OpenAI Chatbot!")
    print("For exit, type  'exit' to exit.")
    api_key = os.getenv("OPENAI_API_KEY", default=None)
    if api_key is None:
        print("Please set your OPENAI_API_KEY environment variable.😢😢")
        return

    model = os.getenv("OPENAI_API_MODEL", default="gpt-3.5-turbo")
    service = OpenAIAPIService(api_key, model)
    while True:
        print("Enter 😁 a prompt for Helping You:")
        prompt = input("> ")
        print(await service.send_message(prompt))
        if prompt.lower() == "exit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
