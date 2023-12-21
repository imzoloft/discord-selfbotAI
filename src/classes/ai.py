import os, openai, asyncio

import utils.file as file
import utils.input as input

class AI:
    def __init__(self, user_id: str, username: str):
        self.username = username
        self.conversation_history = file.read_user_conversation(user_id, username)
        print(self.conversation_history)
        asyncio.create_task(self.initialize(user_id))

    async def initialize(self, user_id: str):
        await file.save_conversation_periodically(60, user_id, self.conversation_history)

    def get_answer(self) -> str:
        response = None
        
        input_text = "\n".join(self.conversation_history)

        try:   
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"{input_text}\n: ",
                temperature=1,
                frequency_penalty=0.5,
                presence_penalty=0.5,
                max_tokens=150
            )
            response = response.choices[0].text.strip()
        except Exception as e:
            print(f"Error: {e}")

        return response

    def chat_with_ai(self, message) -> str:
        self.conversation_history.append(f"Human: {input.remove_discord_emote(message)}")

        answer = self.get_answer()

        if answer:
            self.conversation_history.append(f": {answer}")
        else:
            answer = f"Please say again: {self.conversation_history.pop()[7:]}"

        return answer

