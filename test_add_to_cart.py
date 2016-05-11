from model.sizes import Sizes

def test_add_to_cart_from_first_page(app):
    app.choose_item_from_first_page(Sizes.Size116())
    app.add_to_cart()
    app.go_to_cart()
    assert app.is_added_to_cart()

def test_remove_from_cart(app):
    app.remove_from_cart()
    assert app.is_not_added_to_cart()


def test_add_to_cart_from_second_page(app):
    app.go_to_shop_from_cart()
    app.choose_item_from_second_page(Sizes.Size110())
    app.add_to_cart()
    app.go_to_cart()
    assert app.is_added_to_cart()
    app.remove_from_cart()


def test_add_to_cart_from_third_page(app):
    app.go_to_shop_from_cart()
    app.choose_item_from_third_page(Sizes.Size110())
    app.add_to_cart()
    app.go_to_cart()
    assert app.is_added_to_cart()
    app.remove_from_cart()