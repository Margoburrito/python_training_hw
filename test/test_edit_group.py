from model.group import Group


def test_edit_second_group_name(app):
    if app.group.count() < 2:
        app.group.create(Group(name="test1"))
        app.group.create(Group(name="test2"))
    old_groups = app.group.get_group_list()
    group = Group(name="new group")
    group.id = old_groups[1].id
    app.group.edit_second_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[1] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_second_group_header(app):
    if app.group.count() < 2:
        app.group.create(Group(name="test1"))
        app.group.create(Group(name="test2"))
    old_groups = app.group.get_group_list()
    group = Group(name="new group")
    group.id = old_groups[1].id
    app.group.edit_second_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[1] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
