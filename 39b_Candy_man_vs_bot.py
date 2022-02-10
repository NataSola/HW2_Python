# Игра с кончетами. Дано N конфет. 
# Каждый игрок за каждый ход может взять не более M конфет.
# Побеждает игрок,забравший последнюю конфету.

# man vs man

from random import randint, choice

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
    'Основные правила игры: '
    'Нам будет дано некоторое количество конфет, '
    'за один ход мы можем взять не более определённого количества, '
    'о котором мы с вами договоримся. '
    'Итак, начнём!')
            
messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']

def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут?\n')
    player2 = 'Робик'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
    first = input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n')
    if first != 1: first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    if rules[2] == 1: count = 0
    else: count = 1
    if rules[0] % 10 == 1 and 9 > rules[0] > 10: letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10: letter = 'ы'
    else: letter = ''
    while rules[0] > 0:
        if count%2: 
            move = randint(1, rules[1] + 1)
            print(f'Я забираю {move}')
        else:
            print(f'{players[count%2]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -=1
                else: 
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0: print(f'Осталось {rules[0]} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')