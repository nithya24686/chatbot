import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "deepseek/DeepSeek-V3-0324"
if "GITHUB_TOKEN" not in os.environ:
    print("Error: GITHUB_TOKEN environment variable is not set.")
    print("Please set it using: $env:GITHUB_TOKEN='your_token_here' (PowerShell) or export GITHUB_TOKEN='your_token_here' (Bash)")
    exit(1)

token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

messages = [
    SystemMessage("You are a helpful assistant."),
]

print("Chatbot started. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append(UserMessage(user_input))

    response = client.complete(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model
    )

    assistant_response = response.choices[0].message.content
    print(f"Assistant: {assistant_response}")
    
    messages.append(AssistantMessage(assistant_response))

