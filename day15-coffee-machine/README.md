# ☕ Coffee Machine — Python (Day 15)

A command-line coffee machine simulation built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

## What it does

- Accepts **espresso**, **latte**, and **cappuccino** orders.
- Checks available water, milk, and coffee before accepting payment.
- Calculates the value of quarters, dimes, nickels, and pennies.
- Checks whether a payment covers the selected drink, and calculates change.
- Deducts ingredients and records revenue **only after successful payment**.
- Displays an inventory and revenue `report`, and supports `off` to quit.
- Handles unknown menu options and invalid/negative coin counts.

## How to run

Requires **Python 3**. No additional packages required.

```bash
python main.py
```

Try entering `latte`, paying with 10 quarters (a total of $2.50), and then entering `report` to see the remaining ingredients and revenue.

## Testing

```bash
python -m unittest discover -s tests -v
```

The tests check exact-quantity ingredients, insufficient resources, successful/unsuccessful payment, and correct ingredient deductions.

## What I learned

- Nested dictionaries and data access
- Functions, loops, conditionals and return values
- Tracking shared program state with variables
- Checking inputs and handling edge cases
- Connecting payment logic to inventory changes

## About this project

This is my implementation of a learning challenge from Angela Yu's Python bootcamp. The core idea and starter menu/resource data come from the course; I wrote and refined the application logic as practice.

**Author:** [Saviour Fafali Ankugah](https://github.com/Fafali1234557)
