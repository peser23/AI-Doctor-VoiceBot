from dotenv import load_dotenv
import base64
from groq import Groq

load_dotenv()

# Convert image to required format
def encode_image(image_path):
  #IMAGE_PATH = "data/acne.jpg"
  image_file = open(image_path,"rb")
  encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
  return encoded_image

# Setup Multimodal LLM
def analyse_image_with_query(user_query, encoded_image, model):
  client = Groq()
  #model = "meta-llama/llama-4-scout-17b-16e-instruct"
  #user_query = 'look at the picture and diagnose the problem'
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

  return completion.choices[0].message.content


