import os 
import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    organization = os.environ.get("OPENAI_ORGANIZATION")
)

messages = [
    {
        "role": "system",
        "content": "あなたは端的に発言するAIです。"
    },
    {
        "role": "user",
        "content": "こんにちは"
    }
]

res = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(res.choices[0].message.content)
