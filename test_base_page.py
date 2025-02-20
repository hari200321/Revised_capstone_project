"""test_base_page.py"""

from PageObjects.base_page import WebAutomation


URL = "https://www.saucedemo.com/"

#positive test case for valid URL
def test_positive_url():
    test_url = "https://www.saucedemo.com/"
    assert test_url == URL

    print(f"Success{URL} is valid one")

#negative test case for invalid URL
def test_negative_url():
    test_url = "guvi.in"
    assert test_url == URL

# positive login
def test_positive_login():
    assert WebAutomation.login == WebAutomation.login
    print(f"Success{WebAutomation.login} is the valid one")

#login using invalid username
def test_login_with_invalid_username():
    assert WebAutomation.login == WebAutomation.login_using_invalid_name

#Testing whether logout button is functioning or not
def test_functionality_of_logout_btn():
    assert WebAutomation.is_logout_clickable == WebAutomation.is_logout_clickable
    print(f"Success{WebAutomation.is_logout_clickable} is clickable")

#checking the visibility of cart button
def test_visibility_cart_btn():
    assert WebAutomation.visibility_of_cart_button == WebAutomation.visibility_of_cart_button
    print(f"Success{WebAutomation.visibility_of_cart_button} is visible")