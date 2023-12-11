"""This is the API service that will be used to send requests to OpenAI's API"""
import aiohttp

from models import ChatCompletionResult


class OpenAIAPIService:
    """
    This is the API service that will be used to send requests to OpenAI's API
    """
    OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

    def __init__(self, api_key=None, model=None):
        self.api_key = api_key
        self.model = model

    def compose_message(self, message):
        """
        Compose the message to be sent to the API
        :param message:
        :return:
        """
        return [{"role": "user", "content": message}]

    @property
    def auth_headers(self):
        """
        https://platform.openai.com/docs/api-reference/authentication for AUTH

        curl https://api.openai.com/v1/chat/completions \
         -H "Content-Type: application/json" \
          -H "Authorization: Bearer $OPENAI_API_KEY" \
          -d '{
             "model": "gpt-3.5-turbo",
             "messages": [{"role": "user", "content": "Say this is a test!"}],
             "temperature": 0.7
           }'
        :return:
        """
        return {
            "Authorization": f"Bearer {self.api_key}"
        }

    async def send_message(self, message):
        """
        https://platform.openai.com/docs/guides/text-generation/chat-completions-api
        For more information
        :param message:
        :return:
        """
        data = await self.request_prompt(message)
        if data is None:
            return ""

        res = ChatCompletionResult(data)
        return res.first_message_content

    async def request_prompt(self, message):
        """
        Send a request to the OpenAI API
        :param message:
        :return:
        """
        data = None
        try:
            async with aiohttp.ClientSession() as session:
                payload = {
                    "model": self.model,
                    "messages": self.compose_message(message)
                }

                async with session.post(OpenAIAPIService.OPENAI_API_URL, json=payload,
                                        headers=self.auth_headers) as response:

                    data = await response.json()
        except aiohttp.ClientError as e:
            print(f"An error occurred during the request: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return data
