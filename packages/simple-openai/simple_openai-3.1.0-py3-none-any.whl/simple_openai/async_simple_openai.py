"""Async Simple OpenAI API wrapper

The is the async version of the Simple OpenAI API wrapper which uses the [`aiohttp`](https://docs.aiohttp.org/en/stable/index.html) library.

It is intended for use with asyncio applications.  If you are not using asyncio, you should use the [Simple OpenAI API wrapper](/simple_openai/simple_openai/) instead.
"""

from pathlib import Path
import aiohttp

from . import constants
from .models import open_ai_models
from .responses import SimpleOpenaiResponse
from . import chat_manager

class AsyncSimpleOpenai:
    """Async Simple OpenAI API wrapper

    This class implements the Async Simple OpenAI API wrapper.

    To use this class, you need to have an OpenAI API key. You can get one from [Openai](https://platform.openai.com).

    An optional storage path can be provided.  If a storage path is provided, the chat messages will be stored in the directory specified by the storage path.  If no storage path is provided, the chat messages will not be stored.

    Args:
        api_key (str): Your OpenAI API key
        system_message (str): The system message to add to the start of the chat
        storage_path (Path, optional): The path to the storage directory. Defaults to None.

    !!!Example
        ```python
        from simple_openai import AsyncSimpleOpenai
        import asyncio

        async def main():
            # Get the storage path
            storage_path = Path("/path/to/storage")

            # Create a system message
            system_message = "You are a helpful chatbot. You are very friendly and helpful. You are a good friend to have."

            # Create the client
            client = AsyncSimpleOpenai(api_key, system_message, storage_path)

            # Create tasks for the chat response and the image response
            tasks = [
                client.get_chat_response("Hello, how are you?", name="Bob", chat_id="Group 1"),
                client.get_image_url("A cat"),
            ]

            # Wait for the tasks to complete
            for task in asyncio.as_completed(tasks):
                # Get the result
                result = await task

                # Print the result
                if result.success:
                    # Print the message
                    print(f'Success: {result.message}')
                else:
                    # Print the error
                    print(f'Error: {result.message}')

        if __name__ == "__main__":
            # Run the main function
            asyncio.run(main())
        ```
    """
    def __init__(self, api_key: str, system_message: str, storage_path: Path | None = None) -> None:
        self._headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        # Create the chat manager
        self._chat = chat_manager.ChatManager(system_message, storage_path=storage_path)

    async def get_chat_response(self, prompt: str, name: str, chat_id: str = constants.DEFAULT_CHAT_ID) -> SimpleOpenaiResponse:
        """Get a chat response from OpenAI

        An optional chat ID can be provided.  If a chat ID is provided, the chat will be continued from the chat with the specified ID.  If no chat ID is provided, all messages will be mixed into a single list.

        Args:
            prompt (str): The prompt to use for the chat response
            name (str): The name of the user
            chat_id (str, optional): The ID of the chat to continue. Defaults to DEFAULT_CHAT_ID.

        Returns:
            SimpleOpenaiResponse: The chat response, the value of `success` should be checked before using the value of `message`

        """
        # Add the message to the chat
        messages = self._chat.add_message(open_ai_models.ChatMessage(role='user', content=prompt, name=name), chat_id=chat_id).messages        

        # Create the request body
        request_body = open_ai_models.ChatRequest(messages=messages)

        # Open a session
        async with aiohttp.ClientSession(headers=self._headers, base_url=constants.BASE_URL) as session:
            # Send the request
            async with session.post(constants.CHAT_URL, json=request_body.dict()) as response:
                # Check the status code
                if response.status == 200:
                    # Parse the response body
                    response_body = open_ai_models.ChatResponse.parse_raw(await response.text())

                    # Create the response
                    response = SimpleOpenaiResponse(True, response_body.choices[0].message.content)

                    # Add the response to the chat
                    self._chat.add_message(open_ai_models.ChatMessage(role='assistant', content=response.message, name='Botto'))
                else:
                    # Parse the error response body
                    response_body = open_ai_models.ErrorResponse.parse_raw(await response.text())

                    # Create the response
                    response = SimpleOpenaiResponse(False, response_body.error.message)

                # Return the response
                return response

    async def get_image_url(self, prompt: str) -> SimpleOpenaiResponse:
        """Get an image response from OpenAI

        Args:
            prompt (str): The prompt to use

        Returns:
            SimpleOpenaiResponse: The image response, the value of `success` should be checked before using the value of `message`
        """
            
        # Create the request body
        request_body = open_ai_models.ImageRequest(prompt=prompt)

        # Open a session
        async with aiohttp.ClientSession(headers=self._headers, base_url=constants.BASE_URL) as session:
            # Send the request
            async with session.post(constants.IMAGE_URL, json=request_body.dict()) as response:
                # Check the status code
                if response.status == 200:
                    # Parse the response body
                    response_body = open_ai_models.ImageResponse.parse_raw(await response.text())

                    # Create the response
                    response = SimpleOpenaiResponse(True, response_body.data[0].url)
                else:
                    # Parse the error response body
                    response_body = open_ai_models.ErrorResponse.parse_raw(await response.text())

                    # Create the response
                    response = SimpleOpenaiResponse(False, response_body.error.message)

                # Return the response
                return response
