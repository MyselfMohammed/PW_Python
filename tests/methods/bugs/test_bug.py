import pytest

@pytest.mark.xfail(reason="BUG-1234: Invalid password redirects to Dashboard")
def test_invalid_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("WrongPassword")
    page.get_by_role("button", name="Login").click()

    assert page.get_by_text("Invalid credentials").is_visible() 
       

@pytest.mark.xfail(reason="Feature under development")
def test_forgot_password(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_text("Forgot your password?").click()

    assert page.url.endswith("/requestPasswordResetCode")