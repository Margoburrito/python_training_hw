from model.contact import Contact
import random


def test_edit_contact_name(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.add_new(Contact(firstname="test"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    new_contact = Contact(firstname="Michael", id=old_contacts[index].id)
    app.contact.edit_contact_name_by_id(contact.id, new_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contacts_list()
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contacts_list(), key=Contact.id_or_max)


#def test_edit_contact_worktel(app):
 #   if app.contact.count() == 0:
  #      app.contact.add_new(Contact(firstname="test"))
  #  old_contacts = app.contact.get_contacts_list()
  #  index = randrange(len(old_contacts))
#    contact = Contact(work_tel="332255")
  #  contact.id = old_contacts[index].id
  #  app.contact.edit_contact_worktel_by_index(index, contact)
  #  new_contacts = app.contact.get_contacts_list()
  #  assert len(old_contacts) == len(new_contacts)
  #  old_contacts[index] = contact
  #  assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)