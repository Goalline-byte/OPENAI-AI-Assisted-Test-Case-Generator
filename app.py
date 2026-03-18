import os 
from dotenv import load_dotenv
from openai import OpenAI



load_dotenv() 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", 
         "content": "Generate 5 simple test cases for an e-commerce website's shopping cart functionality."
         }
    ]
)

print(response.choices[0].message.content)