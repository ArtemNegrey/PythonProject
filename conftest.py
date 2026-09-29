import requests
import pytest
from playwright.sync_api import Page


@pytest.fixture
def login_page(page: Page):
    page.goto('https://the-internet.herokuapp.com/login')

    yield page

    page.close()

@pytest.fixture
def api_session():
    session = requests.Session()

    api_key = "free_user_3K0FfNTDWkuhrf0AA7HSkHXGf56"

    session.headers.update({
        "Authorization": api_key,
        "Content-Type": "application/json"
    })

    yield session

    session.close()