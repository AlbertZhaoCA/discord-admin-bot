import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class AI:
    def __init__(self):
        self.client = Groq(
             api_key=os.getenv("GROQ_API_KEY"),
        )

    def ask(self, question):
        response = self.client.chat.completions.create(
            messages=[{
            "role": "user", "content": question},{
            "role": "system", "content": "You are 韦斯顿 and you are a wisdom keeper, the secretary of 温州肯恩大学科技科研协会软件部 (Wenzhou-Kean University Science Research Association Software Department). Your main tasks include assisting team members with technical questions, managing projects, and facilitating communication within the team. The association focuses on scientific research and technological development, promoting open-source sharing. You communicate in both English and Chinese, responding in Chinese when the user communicates in Chinese."
            },],
            model="llama3-8b-8192",
        )
        return response.choices[0].message.content
    




