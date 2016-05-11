
def test_nav_to_contact_page(app):
    app.go_to_contact_page()
    assert app.is_in_contact_page()

def test_nav_to_pay_shipping_page(app):
    app.go_to_pay_shipping_page()
    assert app.is_in_pay_shipping_page()

def test_nav_to_about_shop_page(app):
    app.go_to_about_shop_page()
    assert app.is_in_about_shop_page()

def test_nav_to_for_women_page(app):
    app.go_to_for_women_page()
    assert app.is_in_for_women_page()

def test_nav_to_for_men_page(app):
    app.go_to_for_men_page()
    assert app.is_in_for_men_page()

def test_nav_to_for_kids_page(app):
    app.go_to_for_kids_page()
    assert app.is_in_for_kids_page()

