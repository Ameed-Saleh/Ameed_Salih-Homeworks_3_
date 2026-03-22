import random
import time
MAROON = "\033[07m"
PURPLE = "\033[1;35m"
CYAN = '\033[1;36m'
GREEN = "\033[92m"
RED = '\033[1;31m'
BLACK = "\033[0;30m"
BOLD = "\033[1m"
LIME = "\033[93m"
RESET = '\033[0m'

_rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]

def get_lucky_symbols()->list:
    '''
    this function is used to get lucky symbols
    :return: list of three lucky symbols
    '''
    symbol = []
    for i in range(3):
        symbol.append(random.randint(0, len(symbols) - 1))
    return symbol

def play_game()->None:
    money = 50
    print(f"\n{MAROON}>>>>>>  SLOT MACHINE  <<<<<< {RESET}")
    while money > 0:
        time.sleep(1.5)
        print(f"\n{LIME}Current Balance: {RED}${money}{RESET}")

        bet_input = input(f"{PURPLE}Enter your bet or ('q' to quit): {RESET}").lower()
        if bet_input == 'q':
            break
        if not bet_input.isdigit():
            print(f"\n{RED}Please enter a number.{RESET}")
            continue
        bet = int(bet_input)
        if bet < 1 or bet > money:
            print(f"\n{RED}Invalid bet! Must be between 1 and {money}.{RESET}")
            continue

        s1, s2, s3 = get_lucky_symbols()
        print(f"\n{CYAN}>>>  {symbols[s1]} | {symbols[s2]} | {symbols[s3]}  <<<{RESET}")
        time.sleep(1)
        if s1 == s2 == s3:
            rate = _rate[s1]
            winnings = bet * 777 * rate
            money += winnings
            print(f"{GREEN}\nGood! 3 of a kind {symbols[s1]}! You won {RED}${winnings}{RESET}")

        elif s1 == s2 or s2 == s3 or s1 == s3:
            if s1 == s2 or s1 == s3:
                symbol_rate = s1
            else:
                symbol_rate = s2
            rate = _rate[symbol_rate]
            winnings = bet * rate
            money += winnings
            print(f"{CYAN}\nNice! 2 of a kind {symbols[symbol_rate]}! You won {RED}${winnings}{RESET}")
        else:
            money -= bet
            print(f"{CYAN}\nNo match. You lost {RED}${bet}.{RESET}")

        print("-" * 34)
    print(f"{RED}\nGame Over! You are leaving with ${money}. Thanks for playing bro!{RESET}")
play_game()