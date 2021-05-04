# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group_hw(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="address", header="address", footer="address"))
    app.session.logout()


def test_add_empty_group_hw(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
