from prompt import get_value, get_position
from engine import add, is_game_over,computer_step
from state import show


BOARD_SIZE = 3
grid = [ [None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

print("Hello!")
print("Welcome to XO game!!!")
play = input("you want to play against the computer?(Yes or No) ").lower()
USER_VALUES = {'user1': get_value()}
USER_VALUES['user2'] = 1 - USER_VALUES['user1']
turn = 'user1' if USER_VALUES['user1'] == 1 else 'user2'
show(grid)
while True:
    print(turn.upper(), 'turn')
    pos = get_position(grid)
    add(grid, USER_VALUES[turn], pos)
    show(grid)
    status = is_game_over(grid)
    if status:
        print(turn.upper(), 'won')
        break
    if play == "yes":
        computer_step(grid, USER_VALUES['user2'])
        show(grid)
        status = is_game_over(grid)
        if status:
            print(turn.upper(), 'won')
            break
        continue
    turn = 'user1' if turn == 'user2' else 'user2'