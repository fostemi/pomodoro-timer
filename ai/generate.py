"""
Script that will generate files in the src/ directory.
This will provied options to create files and run code in the 
src/ directory.
"""
import os

from openai import OpenAI

def generateCode():
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "user", "content": "write a haiku about ai"}
        ]
    )
    print(completion)

generateCode()
