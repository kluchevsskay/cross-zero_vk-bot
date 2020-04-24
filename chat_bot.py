import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time

# API-ключ
TOKEN = "114c7052434868862e6a2a38c9b643781bc1aa968fab18720423548aa9968993d6dd72d28e6ede0d64c8e"

vk = vk_api.VkApi(
    token=TOKEN)

vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send",
                          {"peer_id": id, "message": "салам-пополам! Желаешь сыграть в кретики-нолики?", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "да":
                vk.method("messages.send", {"peer_id": id, "message": "Что ж, сам напросился",
                                            "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "нет":
                vk.method("messages.send", {"peer_id": id, "message": "Тогда прощай, Путник",
                                            "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "Ты опе4атался или же ты именно это имел в виду?", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
