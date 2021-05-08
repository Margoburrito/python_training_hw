from model.group import Group


def test_edit_second_group_name(app):
    app.group.edit_second_group(Group(name="new group"))


def test_edit_second_group_header(app):
    app.group.edit_second_group(Group(header="new group"))
