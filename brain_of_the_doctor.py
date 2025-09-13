from dotenv import load_dotenv
import base64
from groq import Groq

load_dotenv()

# Convert image to required format
IMAGE_PATH = "data/acne.jpg"
image_file = open(IMAGE_PATH,"rb")
encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Setup Multimodal LLM
client = Groq()
model = "meta-llama/llama-4-scout-17b-16e-instruct"
user_query = 'look at the picture and diagnose the problem'
completion = client.chat.completions.create(
    model=model,
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": user_query
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data: image/jpeg;base64,{encoded_image}"
            }
          }
        ]
      }
    ]
)

print(completion.choices[0].message.content)


