# from transformers import pipeline

# generator = pipeline("text2text-generation", model="google/flan-t5-large")
# prompt = "what is the meaning of life?"
# output = generator(prompt, max_length=100)
# print(output[0]['generated_text'])
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "qwen/qwen3-0.6b-04-28:free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ],
    
  })
)
response_json = response.json()  # converts response text to dict

# Print the full JSON (optional)
print(json.dumps(response_json, indent=2))

# Usually, the actual answer is nested in the JSON response under something like:
# response_json["choices"][0]["message"]["content"]

answer = response_json["choices"][0]["message"]["content"]
print("Answer from API:", answer)