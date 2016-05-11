from model.sizes import Sizes

def test_cancel_remove_from_cart(app):
    app.go_to_shop_from_cart()
    app.choose_item_from_first_page(Sizes.Size116())
    app.add_to_cart()
    app.go_to_cart()
    app.remove_from_cart()
    app.cancel_remove()
    assert app.is_added_to_cart()
    app.remove_from_cart()

