from model.sizes import Sizes
from model.orders import Orders

def test_registration_order(app):
    app.choose_item_from_first_page(Sizes.Size116())
    app.add_to_cart()
    app.go_to_cart()
    app.go_to_registration()
    app.registration_order(Orders.random())
    assert app.is_registrated()

