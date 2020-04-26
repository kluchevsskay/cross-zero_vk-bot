import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time

# API-ключ
from game_functional import realisation_of_steps

TOKEN = "114c7052434868862e6a2a38c9b643781bc1aa968fab18720423548aa9968993d6dd72d28e6ede0d64c8e"

vk = vk_api.VkApi(
    token=TOKEN)

vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:

            # определение id юзера
            id = messages["items"][0]["last_message"]["from_id"]

            # определение текста последнего сообщения
            body = messages["items"][0]["last_message"]["text"]

            # определение последнего сообщения от бота для некоторых ситуаций
            last_sms_of_bot = ''

            # списки различных вариаций ответа юзера
            yes_list = ['да', 'ага', 'хочу', 'желаю', 'безусловно', 'конечно', '+', 'йес', 'уес', 'yes', 'допустим',
                        'oui', 'уи', 'так точно', 'ок', 'окей', 'ok']
            no_list = ['не', 'нет', 'не хочу', 'не желаю', '-', 'no', 'ноу']
            hello_list = ['хай', 'привет', 'салам', 'здравствуй', 'здравия желаю', 'добрый день', 'бонжур', 'bounjour']
            bye_list = ['пока', 'до свидания', 'прощай', 'bye', 'бай', 'оревуар']
            special_list = ['jjba', 'jojo', 'джоджо', 'джёджё', 'жожо', 'жожа']

            # структура различных ответов на почти всевозможные сообщения от юзера
            if body.lower() in hello_list and last_sms_of_bot != 'пока':
                vk.method("messages.send",
                          {"peer_id": id, "message": "салам-пополам! Желаешь сыграть в кретики-нолики?",
                           "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'привет'

            if body.lower() in hello_list and last_sms_of_bot == 'пока':
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": "и вновь салам-пополам! Тебе снова захотелось провести своё время"
                                      " за игрой в кретики-нолики против меня?",
                           "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'привет'

            elif body.lower() in yes_list and last_sms_of_bot == 'опечатка':
                vk.method("messages.send", {"peer_id": id,
                                            "message": "тогда я закрою глаза на это сообщение и жду"
                                                       " от тебя более внятного ответа :)",
                                            "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'старт'

            elif body.lower() in yes_list and last_sms_of_bot != 'опечатка':
                vk.method("messages.send",
                          {"peer_id": id, "message": "что ж, сам напросился. За кого будешь играть? Отправь Х или 0",
                           "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'старт'

            # начало игры
            elif body.lower() == 'x':
                vk.method("messages.send",
                          {"peer_id": id,
                           "message": "окей, ты крестик, а я нолик. Начинаем! Сейчас генератор определит, "
                                      "кто ходит первым",
                           "random_id": random.randint(1, 2147483647)})
                realisation_of_steps.players_letter('x')
                if realisation_of_steps.first_step() == 'комп':
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": "к счастью, я хожу первым",
                               "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": "к сожалению, ты ходишь первым",
                               "random_id": random.randint(1, 2147483647)})



            elif body.lower() in special_list:
                vk.method("messages.send", {"peer_id": id,
                                            "message": "ゴゴゴゴ Яре-Яре, мой друг."
                                                       " ORA-ORская отсылка засчитана! ",
                                            "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'жожа'

            elif body.lower() in bye_list:
                vk.method("messages.send", {"peer_id": id, "message": "au revoir, mon ami! :)",
                                            "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'пока'

            elif body.lower() in no_list and last_sms_of_bot != 'опечатка':
                vk.method("messages.send", {"peer_id": id, "message": "тогда прощай, Путник",
                                            "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'пока'

            elif body.lower() in no_list and last_sms_of_bot == 'опечатка':
                vk.method("messages.send",
                          {"peer_id": id, "message": "охх, мне с каждым разом всё сложнее тебя понимать, Приятель",
                           "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'непонимание'

            # условие получение не предусмотренного мною ответа
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "ты опе4атался или же ты именно это имел в виду?",
                           "random_id": random.randint(1, 2147483647)})
                last_sms_of_bot = 'опечатка'

    except Exception as E:
        time.sleep(0.5)
