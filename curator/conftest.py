import pytest
from django.test import Client

from curator.lists.models import List, ListItem
from curator.users.models import User


@pytest.fixture()
def user_data():
    return {
        "email": "kazuma@example.com",
        "name": "Kazuma",
        "nickname": "Trash",
        "password": "password",
    }


@pytest.fixture()
def user(user_data):
    return User.objects.create(
        email=user_data["email"], name=user_data["name"], nickname=user_data["nickname"]
    )


@pytest.fixture()
def user_client():
    c = Client()
    c.login(email=user_data["email"], password=user_data["password"])
    return c


@pytest.fixture()
def curated_list(user):
    return List.objects.create(title="Safest Villages", curator=user)
