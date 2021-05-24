from model.contact import Contact


def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Michael")
    contact.id = old_contacts[0].id
    app.contact.edit_contact_name(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_contact_worktel(app):
 #   if app.contact.count() == 0:
  #      app.contact.add_new(Contact(firstname="test"))
  #  old_contacts = app.contact.get_contacts_list()
  #  contact = Contact(work_tel="332255")
  #  contact.id = old_contacts[0].id
  #  app.contact.edit_contact_worktel(contact)
  #  new_contacts = app.contact.get_contacts_list()
  #  assert len(old_contacts) == len(new_contacts)
  #  old_contacts[0] = contact
  #  assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)