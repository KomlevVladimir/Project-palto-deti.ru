

def test_view_item(app):
    app.go_to_home_page()
    app.view_item()
    assert app.item_is_viewed()
    app.get_zoom_image()
    assert app.image_is_zoomed()