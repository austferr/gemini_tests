# Resources

**Gemini AI**

[Google AI Studio](https://aistudio.google.com/)

[Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

[Google Cloud API Platform](https://console.cloud.google.com/apis/dashboard)

**Prompt Engineering**

[Prompt Engineering Guide](https://www.promptingguide.ai/)

[Gemini Reference Sheet](https://www.promptingguide.ai/models/gemini)

[Text Generation](https://ai.google.dev/gemini-api/docs/text-generation?lang=python)

[Gemini 2.0 API Reference](https://ai.google.dev/gemini-api/docs/models/gemini-v2)

-----

## API

> **GENERATE KEYS**
> 
> [API Dashboard](https://console.cloud.google.com/apis/dashboard)


-----

# Prompting

```

pip install -q -U google-generativeai

```

## Simple Request

```

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("prompt")
print(response.text)

```

## Adding Configuration

```

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("prompt")

print(response.text)

```

## Few Shot Prompting with Sentiment Analysis

```

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

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)

```

## Few Shot Prompting using Images

```

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def upload_to_gemini(path, mime_type=None):

  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

files = [
  upload_to_gemini("image_marketing_description_writer1.jpeg", mime_type="image/jpeg"),
  upload_to_gemini("image_marketing_description_writer2.jpeg", mime_type="image/jpeg"),
  upload_to_gemini("image_marketing_description_writer3.jpeg", mime_type="image/jpeg"),
]

response = model.generate_content([
  "Given an image of a product and its target audience, write an engaging marketing description",
  "Product Image: ",
  files[0],
  "Target Audience: Mid-aged men",
  "Marketing Description: Introducing the epitome of power and sophistication - the sleek and captivating sports car. It's more than just a car; it's a symbol of your passion for life and your unwavering commitment to excellence. Embrace the thrill and indulge in the ultimate driving pleasure.",
  "Product Image: ",
  files[1],
  "Target Audience: Environmentalists",
  "Marketing Description: Looking for a sustainable and eco-friendly way to get around? Look no further than this black bicycle. Biking is a great way to reduce your carbon footprint and improve your health at the same time. If you're an environmentalist, there's no better way to get around than by bike!",
  "Product Image: ",
  files[2],
  "Target Audience: Athletes",
  "Marketing Description: ",
])

print(response.text)

```