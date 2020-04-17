import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def main():
    # API-ключ созданный ранее
    token = ""

    # Авторизуемся как сообщество
    vk = vk_api.VkApi(token=token)
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('ноу', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('йес', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()

    # Переход на вторую строку
    keyboard.add_location_button()
    keyboard.add_line()
    keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=")
    keyboard.add_line()
    keyboard.add_vkapps_button(app_id=6979558,
                               owner_id=-181108510,
                               label="Отправить клавиатуру",
                               hash="sendKeyboard")

    def write_msg(user_id, message):
        """ ответ пользователю"""

        vk.method('messages.send', {'user_id': user_id, 'message': message, 'keybord': keyboard.get_keyboard()})

    # Работа с сообщениями
    longpoll = VkLongPoll(vk)

    # Основной цикл
    for event in longpoll.listen():

        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:

            # Если оно имеет метку для меня( то есть бота)
            if event.to_me:

                # Сообщение от пользователя
                request = event.text

                # Каменная логика ответа
                if request.lower() == "привет":
                    write_msg(event.user_id, "Салам-пополам, дружище. Не хочешь ли сыграть в крестики-нолики, ммм",
                              keyboard)
                elif request.lower() == "пока":
                    write_msg(event.user_id, "До свидания, путник :)")
                else:
                    write_msg(event.user_id, "Ты опечатался или хотел сказать именно это?")


if __name__ == '__main__':
    main()
