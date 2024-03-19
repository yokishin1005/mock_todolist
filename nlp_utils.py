from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_= load_dotenv(find_dotenv())

openapi_key = os.getenv('OPENAI_API_KEY')

def predict_category(title, description):
    prompt = f"Predict the category for the following task:\nTitle: {title}\nDescription: {description}\nCategory:"
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    category = completion.choices[0].message.content.strip()
    return category

