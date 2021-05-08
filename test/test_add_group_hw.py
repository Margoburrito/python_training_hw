# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group_hw(app):
    app.group.create(Group(name="address", header="address", footer="address"))


def test_add_empty_group_hw(app):
    app.group.create(Group(name="", header="", footer=""))
