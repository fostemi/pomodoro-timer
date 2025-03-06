import os

from openai import OpenAI

def get_completion(prompt):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    completion = client.chat.completions.create(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion
