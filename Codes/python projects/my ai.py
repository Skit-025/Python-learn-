import openai

class AgenticAI:
    def __init__(self, api_key):
        self.api_key = api_key

    def respond(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
