'''
Question 3 -- BONUS – Casino Slot Machine
Starter code:

rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50
print("=== SLOT MACHINE === \n")
Goal: build a slot machine with 3 spinning slots

Rules:
Each spin shows 3 random symbols
The player starts with 50 money
Before each spin, ask the user how much they want to bet
The bet must be between 1 and the current money
The user can choose to quit the game
Update the player’s money after each round
Winning rules:

All 3 symbols different → player loses the bet
2 of a kind → player gets bet * rate
3 of a kind → player gets bet * 777 * rate
Spin examples:

🍒 🍋 ⭐ → all different → lose
💎 💎 🍋 → 2 of a kind → win bet * 11
⭐ ⭐ ⭐ → 3 of a kind → win bet * 777 * 9
🔔 🍒 🔔 → 2 of a kind → win bet * 7
Important:🎰

The correct rate depends on the matching symbol
Example: 3 × 🍋 → use rate 3
Example: 2 × 💎 → use rate 11
Game ends when:

The player chooses to quit
OR the player runs out of money
Hints:

Use random.choice or random.randint
Keep track of symbol indexes to match the correct rate
First check for 3 matches, then for 2 matches
'''

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

casino_table = {
    "🍒": 2,
    "🍋": 3,
    "⭐": 9,
    "🔔": 7,
    "💎": 11
}

symbols = list(casino_table.keys())

def get_lucky_symbols():
    symbol = []
    for i in range(3):
        symbol.append(random.choice(symbols))
    return symbol

def play_game():
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
        print(f"\n{CYAN}>>>  {s1} | {s2} | {s3}  <<<{RESET}")
        time.sleep(1)
        if s1 == s2 == s3:
            rate = casino_table[s1]
            winnings = bet * 777 * rate
            money += winnings
            print(f"{GREEN}\nGood! 3 of a kind {s1}! You won {RED}${winnings}{RESET}")

        elif s1 == s2 or s2 == s3 or s1 == s3:
            if s1 == s2 or s1 == s3:
                symbol_rate = s1
            else:
                symbol_rate = s2

            rate = casino_table[symbol_rate]
            winnings = bet * rate
            money += winnings
            print(f"{CYAN}\nNice! 2 of a kind {symbol_rate}! You won {RED}${winnings}{RESET}")
        else:
            money -= bet
            print(f"{CYAN}\nNo match. You lost {RED}${bet}.{RESET}")

        print("-" * 34)
    print(f"{RED}\nGame Over! You are leaving with ${money}. Thanks for playing bro!{RESET}")
play_game()