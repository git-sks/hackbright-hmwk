"""Randomly pick customer and print customer info"""

# Add code starting here
import customers
from random import choice

# Hint: remember to import any functions you need from
# other files or libraries

def pick_winner(customers_pool):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers_pool)

    print("Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        ))


def run_raffle():
    """Run the weekly raffle."""

    raffle_pool = customers.get_customers_from_file("customers.txt")
    pick_winner(raffle_pool)


# Run the raffle if call raffle.py
if __name__ == '__main__':
    run_raffle()