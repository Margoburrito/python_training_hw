# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group_hw(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="address", header="address", footer="address"))
    app.logout()

def test_add_empty_group_hw(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()