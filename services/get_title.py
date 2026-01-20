from ollama import chat, ChatResponse

def get_chat_title(model: str, user_query: str) -> str:
    """
    Generate a short, clear title for a user query using Ollama LLM.
    """
    # Construct the prompt for the title
    title_prompt = (
        "You are a helpful assistant that generates short, clear, and catchy titles.\n\n"
        "Task:\n"
        "- Read the given user query.\n"
        "- Create a concise title (max 7 words).\n"
        "- The title should summarize the intent of the query.\n"
        "- Avoid unnecessary words, punctuation, or filler.\n"
        "- Keep it professional and easy to understand.\n\n"
        f"User Query:\n{user_query}\n\n"
        "Output:\nTitle:"
    )

    # Call Ollama chat API
    response: ChatResponse = chat(
        model=model,
        messages=[{'role': 'user', 'content': title_prompt}] # seconds, adjust as needed
    )

    # Extract the content from the response
    title = response['message']['content']
    return title.strip()

# print(get_chat_title("gemma2:2b","compatibility of an istp 8w9 leo and a virgo intj girl"))