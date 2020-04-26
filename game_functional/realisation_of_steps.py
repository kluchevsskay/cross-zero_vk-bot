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


def play_again(answer):
    """сыграть ещё раз"""

    return answer.lower().startswith('д')


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


def get_comp_move(board, computer_letter):
    """копия содержимого доски и хода компа. Исходя из этого определяет куда двигаться и возвращает ход """

    if computer_letter == 'x':
        player_letter = 'o'
    else:
        player_letter = 'x'

    # проверка на возможный выигрыш игрока
    for i in range(1, 10):
        copy = board_copy(board)
        if player_can_make_this_step(copy, i):
            make_step(copy, player_letter, i)
            if player_won(copy, player_letter):
                return i

    # комп старается занять один из свободных углов
    step = random_step(board, [2, 4, 6, 8])
    if step is not None:
        return step

    # старается занять центр, если он свободен, конечно же
    if player_can_make_this_step(board, 5):
        return 5

    # одну из боковых клеток
    return random_step(board, [2, 4, 6, 8])


def is_board_full(board):
    """проверка на заполнение поля"""

    for i in range(1, 10):
        if player_can_make_this_step(board, i):
            return False
        return True


def draw_board(board):
    """ рисование игровой доски в символьной графике"""
    print(' | |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' | |')
    print('---+---+---')
    print(' | |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' | |')
    print('---+---+---')
    print(' | |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' | |')


while True:
    the_board = [' '] * 10
    player_letter, computer_letter = players_letter()
    turn = first_step()
    game_is_playing = True

    while game_is_playing:
        if turn == 'игрок':
            # ход игрока

            draw_board(the_board)
            move = get_player_step(the_board)
            make_step(the_board, player_letter, move)

            if player_won(the_board, player_letter):
                draw_board(the_board)
                game_is_playing = False

            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    break
                else:
                    turn = 'комп'

        else:
            # ход игрока
            move = get_comp_move(the_board, computer_letter)
            make_step(the_board, computer_letter, move)
            if player_won(the_board, computer_letter):
                draw_board(the_board)
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    break
                else:
                    turn = 'игрок'
    if not play_again():
        break
