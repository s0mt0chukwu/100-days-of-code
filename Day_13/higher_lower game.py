# display art
from art import logo, vs
from game_data import data
import random



def format_data(account):
    """Take the account data and return the printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take user's guess and follower count and return if they answered correctly"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
score = 0
game_should_continue = True

# making the account at position B becomes account in position A in the next question
account_b = random.choice(data)


# make the game repeatable
while game_should_continue:
    # generate a random account from game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_a = random.choice(data)

    print(f"compare A {format_data(account_a)}")
    print(vs)
    print(f"against B {format_data(account_b)}")

    # ask user to guess
    guess = input("who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)


    ## get follower count for each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"you're right! current score {score}")
    else:
        print(f"sorry, that's wrong. final score {score}")
        game_should_continue = False

