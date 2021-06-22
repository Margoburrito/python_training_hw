from model.contact import Contact
import random
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(app.group.get_contacts_list()) == 0:
        app.contact.add_new(Contact(firstname="test"))
    contacts = app.contact.get_contacts_list()
    contact = random.choice(contacts)
    app.contact.add_to_group(contact.id)
    db_contacts = db.get_contacts_in_group(Group(id="122"))
    assert contacts == db_contacts

