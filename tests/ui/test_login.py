from playwright.sync_api import expect, Page


def test_successful_login(login_page: Page):
    page = login_page

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    success_message = page.locator("id=flash")

    expect(success_message).to_be_visible()
    expect(success_message).to_contain_text("You logged into a secure area!")


def test_failed_login(login_page: Page):
    page = login_page

    page.get_by_label("Username").fill("testlogin")
    page.get_by_label("Password").fill("testpassword")
    page.get_by_role("button", name="Login").click()

    error_message = page.locator("id=flash")

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Your username is invalid!")