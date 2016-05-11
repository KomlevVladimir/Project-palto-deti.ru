from model.sizes import Sizes


def test_edit_and_update_cart(app):
    app.go_to_shop_from_cart()
    app.choose_item_from_second_page(Sizes.Size122())
    app.add_to_cart()
    app.go_to_cart()
    app.edit_cart()
    app.update_cart()
    assert app.is_edited_cart()
    app.remove_from_cart()