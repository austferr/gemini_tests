
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
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="Skew towards an empathetic feeling for the statement.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Analyze the sentiment of the following statements and classify them as POSITIVE, NEGATIVE, or NEUTRAL. Provide an explanation for the classification. \"There are ants everywhere.\"",
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
        "\"I cannot believe the water is warm.\"",
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
        "\"I want to go home.\"",
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

response = chat_session.send_message("There are birds in the sky, I need to get to my car.")

print(response.text)