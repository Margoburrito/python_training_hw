# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname=u"Александр", middlename=u"Сергеевич", lastname=u"Пушкин", company=u"Царско-сельский лицей", address=u"г. Санкт-Петербург",
                                work_tel="1234567", e_mail="pushkin.as@gmail.com", bday="6", bmonth="June", byear="1799", address2="fhdkhgdk", notes="jfjhflf")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contacts_list()
#    contact = Contact(firstname="", middlename="", lastname="", company="", address="", work_tel="", e_mail="", bday="-", bmonth="-", byear="", address2="", notes="")
#    app.contact.add_new(contact)
#    new_contacts = app.contact.get_contacts_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)