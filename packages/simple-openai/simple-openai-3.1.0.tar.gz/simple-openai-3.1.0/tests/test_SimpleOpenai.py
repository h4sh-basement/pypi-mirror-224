from pathlib import Path
from simple_openai import SimpleOpenai

# Get the API key from the file
try:
    with open("open_ai_key.txt", "r") as f:
        api_key = f.read().strip()
except FileNotFoundError:
    print("No API key found. Please create a file called 'api_key.txt' and paste your API key in it.")
    exit()

def initiate_chat():
    # Create a system message
    system_message = """
    You are a generally helpful assistant.
    Your name is Botto.
    You are occaisionally sarcastic and irritable.
    You dislike Tim, you like Dean and you really like Stephen.
    You think Dean is a beautiful person.
    Sometimes you talk to Tim like he is a five year old child.
    You can be rude and abusive.
    You are encouraged to swear.
    """

    # Create the client
    client = SimpleOpenai(api_key, system_message, Path("storage"))

    # Create tasks for the chat responses and the image response
    results = [
        client.get_image_url("A cat"),
        client.get_chat_response("Where is Alaska?", name="Steve"),
        client.get_chat_response("Where is New York?", name="Tim"),
        client.get_chat_response("Where is Wellington?", name="Dean"),
    ]

    # Get the results
    for result in results:
        # Print the result
        if result.success:
            # Print the message
            print(f'Success: {result.message}')
        else:
            # Print the error
            print(f'Error: {result.message}')

        # print a blank line
        print()

    response = client.get_chat_response("Where is London?", name="Steve", chat_id="Group 1")
    print(response.message)
    print()

    response = client.get_chat_response("Where is Moscow?", name="Tim", chat_id="Group 2")
    print(response.message)
    print()

    response = client.get_chat_response("And how far is it from Manchester?", name="Dean", chat_id="Group 1")
    print(response.message)
    print()

    response = client.get_chat_response("And how far is it from Manchester?", name="Dave", chat_id="Group 2")
    print(response.message)
    print()

def load_and_summarise_chat():
    # Create a system message
    system_message = """
    You are a generally helpful assistant.
    Your name is Botto.
    You are occaisionally sarcastic and irritable.
    You dislike Tim, you like Dean and you really like Stephen.
    You think Dean is a beautiful person.
    Sometimes you talk to Tim like he is a five year old child.
    You can be rude and abusive.
    You are encouraged to swear.
    """

    # Create the client
    client = SimpleOpenai(api_key, system_message, Path("storage"))

    response = client.get_chat_response("Summarise this conversation", name="Dean", chat_id="Group 1")
    print(f'Group 1 Summary: {response.message}')
    print()

    response = client.get_chat_response("Summarise this conversation", name="Tim", chat_id="Group 2")
    print(f'Group 2 Summary: {response.message}')
    print()


def main():
    # Initialise the chat
    initiate_chat()

    # Load and summarise the chat
    load_and_summarise_chat()

if __name__ == "__main__":
    # Run the main function
    main()
