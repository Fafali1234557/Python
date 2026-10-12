"""Small unit tests for the Day 15 project."""
import contextlib
import io
import unittest
from unittest.mock import patch

import main as coffee


class CoffeeMachineTests(unittest.TestCase):
    def setUp(self):
        coffee.resources.update({"water": 300, "milk": 200, "coffee": 100})
        coffee.profit = 0

    def test_exact_ingredients_are_enough(self):
        coffee.resources.update({"water": 50, "milk": 0, "coffee": 18})
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertTrue(coffee.is_resource_sufficient(coffee.MENU["espresso"]["ingredients"]))

    def test_insufficient_resource_is_rejected(self):
        coffee.resources["water"] = 10
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertFalse(coffee.is_resource_sufficient(coffee.MENU["latte"]["ingredients"]))

    def test_insufficient_payment_does_not_increase_profit(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertFalse(coffee.is_transaction_successful(1.00, 2.50))
        self.assertEqual(coffee.profit, 0)

    def test_exact_payment_succeeds(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertTrue(coffee.is_transaction_successful(2.50, 2.50))
        self.assertEqual(coffee.profit, 2.50)

    def test_make_coffee_deducts_resources(self):
        with contextlib.redirect_stdout(io.StringIO()):
            coffee.make_coffee("latte", coffee.MENU["latte"]["ingredients"])
        self.assertEqual(coffee.resources, {"water": 100, "milk": 50, "coffee": 76})

    def test_no_dispense_when_payment_fails(self):
        commands = iter(["latte", "0", "0", "0", "0", "off"])
        with patch("builtins.input", side_effect=lambda _: next(commands)):
            with contextlib.redirect_stdout(io.StringIO()) as output:
                coffee.main()
        self.assertNotIn("Here is your latte!", output.getvalue())
        self.assertEqual(coffee.resources, {"water": 300, "milk": 200, "coffee": 100})


if __name__ == "__main__":
    unittest.main()
