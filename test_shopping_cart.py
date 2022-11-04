from shopping_cart import ShoppingCart
import pytest

def test_can_add_item_to_cart():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()
    

def test_when_add_more_than_max_items_should_fail():
    cart = ShoppingCart(5)
    for _ in range(5):  #first we fill the cart and then we test if we have an overflow
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")

def test_can_get_total_price():   #for testing only one test, on cmd: pytest test_shopping_cart.py:: name_function() -s 
    #pricemap
    #pass for using print (example testing only one func)
    cart = ShoppingCart(5)
    cart.add("apple")
    cart.add("orange")
    price_map = {"apple": 1.0, "orange": 2.0}
    assert cart.get_total_price(price_map) == 3.0
