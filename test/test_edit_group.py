from model.group import Group


def test_edit_second_group_hw(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_second_group(Group(name="group", header="group", footer="group"))
    app.session.logout()