
import os                                                                         # import OS, environment variables.
import google.generativeai as genai                                               # import Gemini library.

genai.configure(api_key=os.environ["GEMINI_API_KEY"])                             # use environment variable GEMINI_API_KEY as api_key.


generation_config = {                                                             # set configuration for request.
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(                                                    # define model and configuration.
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(                                                  # start chat, using defined parameters.
  history=[
  ]
)

response = chat_session.send_message("prompt")                                    # define prompt and request response.

print(response.text)