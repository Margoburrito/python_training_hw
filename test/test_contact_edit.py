from model.contact import Contact


def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test"))
    app.contact.edit_contact_name(Contact(firstname="Michael"))


def test_edit_contact_worktel(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="test"))
    app.contact.edit_contact_worktel(Contact(work_tel="332255"))