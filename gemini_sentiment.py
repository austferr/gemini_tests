
import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="Skew slightly towards NEGATIVE sentiment.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Analyze the sentiment of the following Tweets and classify them as POSITIVE, NEGATIVE, or NEUTRAL. \"It's so beautiful today!\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "POSITIVE",
      ],
    },
    {
      "role": "user",
      "parts": [
        "\"It's so cold today I can't feel my feet...\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "NEGATIVE",
      ],
    },
    {
      "role": "user",
      "parts": [
        "\"The weather today is perfectly adequate.\"",
      ],
    },
    {
      "role": "model",
      "parts": [
        "NEUTRAL",
      ],
    },
  ]
)

response = chat_session.send_message("I can't believe this weather.")

print(response.text)