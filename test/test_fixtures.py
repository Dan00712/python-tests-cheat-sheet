import sample
import sample.shopping_cart
from sample.shopping_cart import ShoppingCart
from sample.shopping_cart import ShoppingItem

import pytest

@pytest.fixture
def test_params():
    return {'name':'tom', 'price':2}

def test_ShoppingItem(test_params):
    item = ShoppingItem(**test_params)
    assert item.name == test_params['name'] and item.price == test_params['price']


@pytest.fixture
def item():
    return ShoppingItem('test', 69)

@pytest.fixture 
def my_list():
    return []

@pytest.fixture
def append_my_list(my_list, item):
    my_list.append(item)

def test_element_my_list(append_my_list, my_list, item):
    # my_list is cached from append_my_list and the same instance is used
    # as such my_list was modified by append_my_list
    # and now has the reference to the item object
    assert my_list[0] is item