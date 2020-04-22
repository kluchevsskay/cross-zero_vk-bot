import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
    # API-ключ
    TOKEN = "114c7052434868862e6a2a38c9b643781bc1aa968fab18720423548aa9968993d6dd72d28e6ede0d64c8e"

    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 'ppuubblliiccc')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Спасибо, что написали нам. Мы обязательно ответим",
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
