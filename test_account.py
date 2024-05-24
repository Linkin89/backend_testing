import pytest
from faker import Faker
from client import Client

@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user_generate():
    fake = Faker("ru_RU")
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
        }


data = [
    {
    #короткий логин
        "login": "p",
        "email": "email123123olo@olo123.ru",
        "password": "fffaaakerpass"
        },
    #невалидный email
        {
        "login": "vadimkololo123",
        "email": "email123123olo@olo@123.ru",
        "password": "fffaaakerpass"
        },
    #короткий пароль
        {
        "login": "vadimkololo123",
        "email": "email123123olo@olo123.ru",
        "password": "s"
        }
]


@pytest.mark.parametrize("data", data)
def test_post_v1_account(data, client):
    response = client.register_user(data)
    assert response.status_code == 400, "Статус код ответа должен быть 400"