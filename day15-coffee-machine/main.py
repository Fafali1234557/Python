"""Day 15 Coffee Machine — a command-line project from 100 Days of Code."""

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, "milk": 0},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100}
profit = 0


def is_resource_sufficient(order_ingredients):
    """Check whether the machine has enough of each ingredient."""
    is_enough = True
    for item, required_amount in order_ingredients.items():
        # Equality is sufficient: 50 ml on hand can supply a 50 ml order.
        if required_amount > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough


def process_coins():
    """Return the total value of US coins entered, or None if invalid."""
    print("Please insert coins.")
    total = 0
    for name, value in (("quarters", 0.25), ("dimes", 0.10),
                        ("nickels", 0.05), ("pennies", 0.01)):
        try:
            count = int(input(f"How many {name}?: "))
        except ValueError:
            print("Please enter a whole number of coins.")
            return None
        if count < 0:
            print("Coin counts cannot be negative.")
            return None
        total += count * value
    return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
    """Check payment and record revenue only on a successful purchase."""
    global profit
    if money_received < drink_cost:
        print(f"Sorry, ${money_received:.2f} is not enough. Money refunded.")
        return False

    profit += drink_cost
    change = round(money_received - drink_cost, 2)
    print(f"Here is your change: ${change:.2f}")
    return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients for a paid order."""
    for item, amount in order_ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}! ☕")


def print_report():
    """Print the remaining supplies and money collected."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit:.2f}")


def main():
    """Keep accepting orders until the machine is switched off."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice == "off":
            break
        if choice == "report":
            print_report()
            continue
        if choice not in MENU:
            print("Please choose espresso, latte, cappuccino, report, or off.")
            continue

        drink = MENU[choice]
        ingredients = drink["ingredients"]
        if not is_resource_sufficient(ingredients):
            continue

        payment = process_coins()
        if payment is not None and is_transaction_successful(payment, drink["cost"]):
            make_coffee(choice, ingredients)


if __name__ == "__main__":
    main()
