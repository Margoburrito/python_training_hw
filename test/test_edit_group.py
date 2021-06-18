from model.group import Group
import random
from random import randrange


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_group = Group(name="new ggyurеyoup", id=old_groups[index].id)
    app.group.edit_group_by_id(group.id, new_group)

    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    index = randrange(len(old_groups))
#    group = Group(name="new group")
#    group.id = old_groups[1].id
#    app.group.edit_second_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[1] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




