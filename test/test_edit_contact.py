from model.contact import Contact
from random import randrange


def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Michael")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_name_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


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