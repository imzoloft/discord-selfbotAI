import json, asyncio

from utils.prompt import create_prompt

def save_user_conversation(user_id: str, conversation_history: list[str]) -> None:
    with open(f"data/conversations/{user_id}.json", "w+") as f:
        json.dump(conversation_history, f)

def read_user_conversation(user_id: str, username: str) -> list[str]:
    try:
        with open(f"data/conversations/{user_id}.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [create_prompt(username)]

async def save_conversation_periodically(time_interval: int, user_id: str, conversation_history: list[str]) -> None:
    while True:
        await asyncio.sleep(time_interval)

        save_user_conversation(user_id, conversation_history)