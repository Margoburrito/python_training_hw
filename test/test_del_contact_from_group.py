from model.contact import Contact
import random
from model.group import Group


def test_del_contact_from_group(app, db, orm_db):
    if len(db.get_contacts_list()) == 0 or len(db.get_groups_with_contacts()) == 0:
        groups = db.get_group_list()
        group = random.choice(groups)
        old_contacts_not_in_groups = orm_db.get_contacts_not_in_group(group)
        contact = random.choice(old_contacts_not_in_groups)
        app.contact.add_to_group(contact=contact, group=group)

    group = random.choice(db.get_groups_with_contacts())
    old_contacts_in_group = orm_db.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    old_contacts_not_in_group = orm_db.get_contacts_not_in_group(group=group)
    app.contact.delete_contact_from_group(contact=contact, group=group)
    new_contacts_in_group = orm_db.get_contacts_in_group(Group(id=group.id))
    new_contacts_not_in_group = orm_db.get_contacts_not_in_group(Group(id=group.id))

    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
    assert len(old_contacts_not_in_group) + 1 == len(new_contacts_not_in_group)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)