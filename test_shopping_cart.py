from shopping_cart import ShoppingCart
import pytest
from item_database import *
from unittest.mock import *

#fixtures - help redure repeating code - passed as an argument
#pytest.fixture - makes it available to pass a function as an argument, in this case object instance Shoppingcart(5)

@pytest.fixture
def cart():
    #All seturp for cart here that will be passed throughout the tests
    #Each shoppingcart is created and passed as new in each test_ it doesnt reuse it
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):

    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    
    cart.add("apple")
    assert "apple" in cart.get_items()
    

def test_when_add_more_than_max_items_should_fail(cart):
    
    for _ in range(5):  #first we fill the cart and then we test if we have an overflow
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")

def test_can_get_total_price(cart):   #for testing only one test, on cmd: pytest test_shopping_cart.py:: name_function() -s 
    #pricemap
    #pass for using print (example testing only one func)
   
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)  #mocking the get method, it will exist, but it hasnt been implemented yet (thaths why we mock)
    assert cart.get_total_price(item_database) == 3.0


