
# gemini_tests
for practicing, testing the Gemini AI API.

-----

## !
an **API key** will need to be generated and added in order to run scripts.

in PowerShell use:

```

setx GEMINI_API_KEY "key"

```

sets a local environment variable that is called using:

```

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

```

if Gemini library needs downloaded:

```

pip install -q -U google-generativeai

```

-----

## gemini_testing.py
*basic test for sending requests.*

replace prompt/question to test.

## gemini_simple.py
*syntax for sending requests to Gemini model.*

directly returns formatted response.

## gemini_sentiment.py
*basic formatting test for setting sentiment analysis.*

directly returns response with a minor explanation.

## py_info.md
*general notes for syntax, prompt engineering, etc.*

examples of syntax and prompts.

-----

### Updates
- updated py_info.md with detailed info.
- added gemini_sentiment.py after testing.
- added comments to gemini_simple.py
- updated README.md.

-----

