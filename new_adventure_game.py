import time
import random


def print_with_delay(statements):
    time.sleep(2)
    print(statements)


def scene1(statements1):
    time.sleep(2)
    print_with_delay(statements1)


def scene2(statements2):
    time.sleep(2)
    print_with_delay(statements2)


start_statements = [
    'You find yourself standing in an open field, filled with grace '
    'and yellow wildflowers',
    'In front of you is a house.',
    'To your right is dark cave.',
    'In your hand hold a trusty (but not very effective) dagger.',
    'Enter 1 to knock on the door of the house.',
    'Enter 2 to peer into the cave',
    'What do you want to do?',
    ]

statements1 = ['You approach the door of the house.',
               'You about to knock when the door opens and out step a gorgon.',
               "Eep! This is the gorgon's house.",
               'The gorgon attacks you!',
               'You feel a bit under-prepared for this, '
               'with only having a tiny dagger.',
               ]

statements2 = ['You approach the cave.',
               'You see something shining in the back',
               'You pick it up and realise its a new shiny dagger',
               'You leave the cave with your new dagger '
               'and walk towards the house.'
               ]

end_game_statement1 = ['You are willing to fight the gorgon']

end_game_statement2 = ['You feel under-prepared and willing to run away',
                       'The gorgon catches you!',
                       'You have lost!']

end_game_statement3 = ['There is no space for you to run away',
                       'You have lost.']


def game_end_one(end_game_statement1):
    for statement in end_game_statement1:
        print_with_delay(statement)


def game_end_two(end_game_statement2):
    for statement in end_game_statement2:
        print_with_delay(statement)


def game_end_three(end_game_statement3):
    for statement in end_game_statement3:
        print_with_delay(statement)


def end_final():
    print('GAME IS OVER!!')


game_over_statement1 = ['The Gorgon attacks you and eats you!',
                        'You Lose!', 'Your game is over1']
game_over_statement2 = ['The Gorgon bites your head off!',
                        'You die and lose!', 'Your game is over2']
game_over_statement3 = ['You never stood a chance!',
                        'Your game is over3']

game_over_runaway_statement1 = \
    ['You ran away, fell over a rock and died', 'You lose!',
     'Your game is over']
game_over_runaway_statement2 = ['You die', 'The gorgon caught you',
                                'You lose!', 'Your game is over']
game_over_runaway_statement3 = ['You never stood a chance!',
                                'Your game is over']

win_runaway_statement1 = \
    ['You ran away, jumped in the river and swam away!',
     'You run back into the field.',
     "Likely, you don't seem to have been followed.", 'You win!']
win_runaway_statement2 = ['You ran away', 'The gorgon never caught you',
                          'You win!', 'Your game is over']
win_runaway_statement3 = ['You ran away', 'The gorgon never stood a chance!',
                          'You so fast!', 'Your game is over']


def random_lost():
    x = random.randint(1, 3)
    if x == 1:
        game_end_one(game_over_statement1)
    elif x == 2:
        game_end_two(game_over_statement2)
    elif x == 3:
        game_end_three(game_over_statement3)
    end_final()


def random_runaway_lost():
    x = random.randint(1, 3)
    if x == 1:
        write(game_over_runaway_statement1)
    elif x == 2:
        write(game_over_runaway_statement3)
    elif x == 3:
        write(game_over_runaway_statement3)
    end_final()


win_statement1 = ['The gorgon attacks',
                  'You spin to the side and stab the gorgon',
                  'Wow, you have won!'
                  ]

win_statement2 = ['You fight and defeat the gorgon!',
                  'Wow you have defeated the opponent.']

win_statement3 = ['You have won, the fight!', 'Your weapon is damaged']


def win1(win_statement1):
    for statement in win_statement1:
        print_with_delay(statement)


def write(info):
    for statement in info:
        print_with_delay(statement)


def win2(win_statement2):
    for statement in win_statement2:
        print_with_delay(statement)


def win3(win_statement3):
    for statement in win_statement3:
        print_with_delay(statement)


def end_with_win():
    print('THE END!!')


def random_win_scenario():
    x = random.randint(1, 3)
    if x == 1:
        win1(win_statement1)
    elif x == 2:
        win2(win_statement2)
    elif x == 3:
        win3(win_statement3)
    end_with_win()


def random_runaway_win_scenario():
    x = random.randint(1, 3)
    if x == 1:
        write(win_runaway_statement1)
    elif x == 2:
        write(win_runaway_statement2)
    elif x == 3:
        write(win_runaway_statement3)
    end_with_win()


def random_outcome_scenario(optionTaken):
    x = random.randint(1, 4)

    print(optionTaken)
    print(x)

    if x == 1 or x == 3 and optionTaken == 'fight':
        random_win_scenario()
    elif x == 1 or x == 2 or x == 3 and optionTaken == 'run':
        random_runaway_lost()
    elif x == 2 or x == 3 and optionTaken == 'fight':
        random_lost()
    elif x == 2 or x == 4 and optionTaken == 'run':
        random_runaway_win_scenario()


def play_game():

    for statement in start_statements:
        print_with_delay(statement)

    response = input('Please enter 1 or 2: ')
    runscenario(response)


def runscenario(response):

    print_with_delay('You chose ' + response + '.')
    print_with_delay("Let't see if you chose wisely.")
    if response == '1':
        enterHouse()
    elif response == '2':
        for statement in statements2:
            scene2(statement)
        enterHouse()
    else:
        response = input('Please renter 1 or 2: ')
        runscenario(response)

    ask_for_replay()


def enterHouse():
    global decision

    for statement in statements1:
        scene1(statement)

    decision = input('Would you like to (1) fight or (2) run away?')
    if decision == '1':
        write(end_game_statement1)
        random_outcome_scenario('fight')
    elif decision == '2':
        random_outcome_scenario('run')
    else:
        decision = input('Please renter 1 or 2: ')
        if decision == '1' or decision == '2':
            statements1.clear()
            enterHouse()
        else:
            decision = input('Please renter 1 or 2: ')


def decide_win_or_defeat():
    if decision == 1:
        random_lost()
    elif decision == 2:
        random_win_scenario()
    else:
        ("oh no, something is wrong.")


def goodbye():
    print_with_delay('see you soon!')
    print('BYE')


def start_over():
    play_game()
    decide_win_or_defeat()
    ask_for_replay()


def ask_for_replay():
    replay = input('do you want to play again? (y/n)')
    if replay == 'y':
        play_game()
    elif replay == 'n':
        goodbye()
    else:
        print("oh no, something is wrong.")
        goodbye()


play_game()
