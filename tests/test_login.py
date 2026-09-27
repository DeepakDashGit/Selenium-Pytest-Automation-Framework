import pytest
from pages.login_page import LoginPage

#Valid Login
def test_valid_login(open_app):
    login_page = LoginPage(open_app)

    login_page.login(
        "Admin",
        "admin123"
    )

    assert "dashboard" in open_app.current_url

#Invalid Username + Password :- instead of repeating the below code again, and again
# we can use  @pytset.mark.parametrize()

# def test_invalid_login(driver):
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     login_page = LoginPage(driver)
#     login_page.login(
#         "InvalidUser",
#         "InvalidPassword"
#     )
#     error_message = login_page.get_error_message()
#     assert "Invalid credentials" in error_message

@pytest.mark.parametrize(
    "username, password",
    [
        ("InvalidUser", "InvalidPassword"),
        ("Admin", "InvalidPassword"),
        ("InvalidUser", "admin123"),
    ]
)
def test_invalid_login(open_app, username, password):

    login_page = LoginPage(open_app)

    login_page.login(username, password)

    error_message = login_page.get_error_message()

    assert "Invalid credentials" in error_message

#Empty Username
def test_empty_username(open_app):

    login_page = LoginPage(open_app)

    login_page.enter_password("admin123")
    login_page.click_login()

    error_message = login_page.get_required_message()


    assert "Required" in error_message

#Empty Password
def test_invalid_password(open_app):

    login_page = LoginPage(open_app)

    login_page.enter_username("Admin")
    login_page.click_login()
    error_message = login_page.get_required_message()
    assert "Required" in error_message

#Empty Username + Empty Password
def test_empty_username_and_password(open_app):

    login_page = LoginPage(open_app)

    login_page.click_login()

    required_messages = open_app.find_elements(
        *login_page.REQUIRED_MESSAGE
    )

    assert len(required_messages) == 2
    