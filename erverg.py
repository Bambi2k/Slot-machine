import random as rand
import random


SYMBOLS = ["💛", "💥", "❌", "⚜", "🟢", "💲"]


print("\n"*5, "Welcome to the slot marchine!", SYMBOLS)


def get_bet(bank):
    print("You have", bank, "dollars in the bank")
    bet = int(input("How much would you like to bet? "))
    return bet


def play():
    bank = 100
    bet = 0
    while bank > 0:
        bet = get_bet(bank)
        bank -= bet
        random_symbols = generate_random_symbols()
        print_symbols(random_symbols)
        max_count = calculate_changefactor(random_symbols)
        multiplier = get_multiplier(max_count)
        winnings = bet*multiplier
        bank += winnings
        print("You have", bank, "dollars")
        play_again = input("Play again? (yes or no) -> ")
        if play_again == "yes" or "Yes" or "YES":
            continue
        else:
            print("You have widthdrawn from the game with",
                  bank, "dollars in your wallet.")
            break


def generate_random_symbols():
    return random.choices(SYMBOLS, k=5)


def calculate_changefactor(random_symbols: list):
    max_count = 0
    for sym in SYMBOLS:
        c = random_symbols.count(sym)
        if c > max_count:
            max_count = c
    return max_count


def get_multiplier(max_count):
    if max_count == 2:
        return 1
    elif max_count == 3:
        return 2
    elif max_count == 4:
        return 4
    elif max_count == 5:
        return 10
    else:
        return 0


def print_symbols(list_of_symbols):
    print(list_of_symbols)


play()
