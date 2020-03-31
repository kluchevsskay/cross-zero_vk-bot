import random


def players_letter(letter):
    """выбор, за кого играть (крестик или нолик)"""

    if letter.lower() == 'x' or letter.lower() == 'х':
        return ['x', 'o']
    else:
        return ['o', 'x']
    # Возвращает список с буквой игрока в качестве первого элемента и буквой компьютера в качестве второго элемента


def first_step():
    """случайное определение, кто ходит первым"""

    if random.randint(0, 1) == 0:
        return 'комп'
    else:
        return 'игрок'


def play_again():
    """сыграть ещё раз"""
    # попробовать сделать взаимодействие с кнопками всплывающей клавы todo
    return True


def make_step(board, letter, step):
    """отметить на начальной схеме шаг"""

    board[step] = letter


def player_won(board, letter):
    """проверка на выигрыш игрока"""

    # Верхняя, средняя, нижняя линия. Левый, центральный, правый столбик. Обе диагонали
    if (board[7] == letter and board[8] == letter and board[9] == letter) or (
            board[4] == letter and board[5] == letter and board[6] == letter) or (
            board[1] == letter and board[2] == letter and board[3] == letter) or (

            board[7] == letter and board[4] == letter and board[1] == letter) or (
            board[8] == letter and board[5] == letter and board[2] == letter) or (
            board[9] == letter and board[6] == letter and board[3] == letter) or (

            board[7] == letter and board[5] == letter and board[3] == letter) or (
            board[9] == letter and board[5] == letter and board[1] == letter):
        return True


def board_copy(board):
    """копируем игровую схему доски"""

    copy_board = []
    for i in board():
        copy_board.append(i)
    return copy_board


def player_can_make_this_step(board, step):
    """проверка на возможность хода"""
    if board[step] == ' ':
        return True


def get_player_step(board):
    """выполнение хода игрока"""

    step = ' '  # получить из сообщения текст
    if step in '1 2 3 4 5 6 7 8 9'.split() and player_can_make_this_step(board, int(step)):
        return int(step)


def random_step(board, steps_list):
    """генерация случайного хода компьютера"""

    possible_steps = []
    for i in steps_list:
        if player_can_make_this_step(board, i):
            possible_steps.append(i)

    if len(possible_steps) != 0:
        return random.choice(possible_steps)
    else:
        return None
