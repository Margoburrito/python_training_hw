from model.group import Group


def test_edit_second_group_name(app):
    if app.group.count() < 2:
        app.group.create(Group(name="test1"))
        app.group.create(Group(name="test2"))
    app.group.edit_second_group(Group(name="new group"))


def test_edit_second_group_header(app):
    if app.group.count() < 2:
        app.group.create(Group(name="test1"))
        app.group.create(Group(name="test2"))
    app.group.edit_second_group(Group(header="new group"))
