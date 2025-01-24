
# gemini_tests
for practicing, testing the Gemini API.

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

-----

## gemini_simple.py
*basic formatting test for sending requests to Gemini model.*

directly returns formatted response.

## py_info.md
*general notes for syntax, prompt engineering, etc.*

-----

### Updates
- merged branches, added README content,
-----

