import sample
import sample.shopping_cart
from sample.shopping_cart import ShoppingCart

import unittest

def test_creation():
    """
        Tests if the Creation via Default Constructor throws an Exception
    """
    cart = ShoppingCart()


class TestShoppingCart(unittest.TestCase):

    def test_creation(self):
        """
            Tests if the Creation via Default Constructor throws an Exception
        """
        cart = ShoppingCart()
