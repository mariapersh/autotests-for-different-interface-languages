import time


def test_check_basket_button_exists(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)
    buttons = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(buttons) == 1, 'Button "add to basket" does not exist'
