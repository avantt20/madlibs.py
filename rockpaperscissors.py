
import random

counterlose = 0
counterwin = 0
countertied = 0
def play():
    user = input("Enter an option ('r' for rock, 'p' for paper, 'sc' for scissors, 'l' for lizard or 'sp' for spock): ").lower()
    computer = random.choice(['r', 'p', 'sc', 'l', 'sp']).lower()
    if user == computer:
        global countertied
        countertied += 1
        return "You tied with the computer"
    if is_win(user, computer):
        global counterwin
        counterwin += 1
        return "You beat the computer!"
    else:
        global counterlose
        counterlose += 1
        return "You lost to the computer bozo"

    # sc>p, p>r, r>l, l>sp, sp>sc, sc>l, p>sp, sp>r, r>sc, l>p

def is_win(player, opponent):
    if (player == 'sc' and opponent == 'p') or (player == 'p' and opponent == 'r') \
        or (player == 'r' and opponent == 'l') or (player == 'l' and opponent == 'sp') \
        or (player == 'sp' and opponent == 'sc') or (player == 'sc' and opponent == 'l') \
        or (player == 'p' and opponent =='sp') or (player == 'sp' and opponent == 'r') \
        or (player == 'r' and opponent == 'sc') or (player == 'l' and opponent == 'p'):
        return True

keep_playing = input("Do you want to keep playing? Y or N: ").lower()

while keep_playing == 'y':
    print(play())
    keep_playing = input("Do you want to keep playing? Y or N: ").lower()
    if keep_playing == 'n':
        print("You have succesfully quit")
        print("You won " + str(counterwin) + " games.") 
        print("You lost " + str(counterlose) + " games.") 
        print("You tied " + str(countertied) + " games.") 