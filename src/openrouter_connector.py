import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

def call_llm(prompt, model = "x-ai/grok-code-fast-1"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
            )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None

def call_vision_llm(model, prompt, image_path):
    """Call LLM with vision capabilities using an image"""
    try:
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        
        image_type = "jpeg" if image_path.lower().endswith(('.jpg', '.jpeg')) else "png"
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/{image_type};base64,{image_data}"
                            }
                        }
                    ]
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None