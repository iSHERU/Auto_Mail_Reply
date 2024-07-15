import requests
import json

API_KEY = 'your_api_key' # you can get one from fireworks

url = "api_key_url" # also from fireworks

def get_mail_reply(email_msg_body, email_sender_name):
  payload = {
    "model": "accounts/fireworks/models/llama-v3-70b-instruct",
    "max_tokens": 1024,
    "top_p": 1,
    "top_k": 40,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "temperature": 0.6,
    "messages": [
    {
      "role": "system",
      "content": "" # give it an identity according to which it can generate responses to the message it will get
    },
    {
      "role": "user",
      "content": f"{email_msg_body}, {email_sender_name}"
    }
    ]
  }
  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
  }
  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

  message_content = json.loads(response.text)
  reply_email = message_content["choices"][0]["message"]["content"]

  return reply_email