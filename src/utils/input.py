import re, emoji

def remove_discord_emote(text: str) -> str:
    return re.sub(r"<\w?:\w+:\d+>", "", text)

def remove_emoji(text: str) -> str:
    return emoji.replace_emoji(text, "")

def remove_discord_emote_and_emoji(text: str) -> str:
    return remove_emoji(remove_discord_emote(text))