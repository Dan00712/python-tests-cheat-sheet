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

#@pytest.fixture(autouse=True)  # this would use append_my_list always, which eliminates the use of the parameter append_my_list, which may reduce 
@pytest.fixture
def append_my_list(my_list, item):
    my_list.append(item)

def test_element_my_list(append_my_list, my_list, item):
    # my_list is cached from append_my_list and the same instance is used
    # as such my_list was modified by append_my_list
    # and now has the reference to the item object
    assert my_list[0] is item


@pytest.fixture(scope='module') # this fixture can be reused in the module and is automatically injected into the .py file; this is useful for network stuff, because it is cached within the module
def module_fixture():
    ...

# function:
#   fixture is destroyed at the end of the test
# class:
#   fixture is destroyed at last destruction of last test in class
# module:
#   fixture is destroyed at last destruction of last test in module
# package:
#   fixture is destroyed at last destruction of last test in package
# session:
#   fixture is destroyed at the end of the test session
# dynamic -> callable to scope
#   callable with fixture_name and config params returns the scope


@pytest.fixture
def yielded_fixture():
    a = 'a'  # Normal Fixture stuff
    yield a  # return is swapped with yield
    del a    # fixture cleanup is placed here; generator returns with send(None)

@pytest.fixture
def manual_finalize(request):

    def inner_finalize():
        ...

    request.addfinalizer(inner_finalize)
    return 'x'

# finalize filo
# fix1, fix2 => fix2.finalize(); fix1.finalize()

