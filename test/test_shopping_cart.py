import sample
import sample.shopping_cart
from sample.shopping_cart import ShoppingCart
from sample.shopping_cart import ShoppingItem

import unittest

def test_creation():
    """
        Tests if the Creation via Default Constructor throws an Exception
    """
    cart = ShoppingCart()

def test_append():
    cart = ShoppingCart()
    item = ShoppingItem('tom', 1)
    cart.append(item)

    assert len(cart._items) == 1 and cart[0] is item

class TestShoppingCart(unittest.TestCase):

    def test_creation(self):
        """
            Tests if the Creation via Default Constructor throws an Exception
        """
        cart = ShoppingCart()

    def test_append(self):
        cart = ShoppingCart()
        item = ShoppingItem('tom', 1)
        cart.append(item)

        self.assertEqual(len(cart._items), 1)
        self.assertTrue(cart[0] is item)
    
    def test_exception(self):
        with self.assertRaises(Exception):
            raise Exception('The Context Manager expects this Exception')
        
        #Exception('This Exception will cause the Test to fail')
