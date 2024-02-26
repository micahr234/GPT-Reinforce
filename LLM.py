from openai import OpenAI


class LLM:

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.messages = []

    def add_context(self, message):
        self.messages.append({"role": "system", "content": message})

    def reply(self):
        completion = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            temperature=0.7,
            n=1,
            presence_penalty=0,
            frequency_penalty=0,
            messages=self.messages,
        )
        if completion.choices[0].finish_reason != 'stop':
            raise "LLM did not finish"
        message = str(completion.choices[0].message.content)
        self.messages.append({"role": "assistant", "content": message})
        return message

    def add(self, message):
        self.messages.append({"role": "user", "content": message})

    def clear(self):
        self.messages = []
