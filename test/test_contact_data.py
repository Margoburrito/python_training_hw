from random import randrange
import re
from model.contact import Contact


def test_data_on_home_page(app, db):
    #index = random(app)
    contact_from_home_page = app.contact.get_contacts_list()
    contact_from_db = db.get_contacts_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
    #assert contact_from_home_page.firstname == contact_from_db.firstname
    #assert contact_from_home_page.lastname == contact_from_db.lastname
    #assert contact_from_home_page.address == contact_from_db.address


#def random(app, db):
 #   contacts = db.get_contacts_list()
 #   index = len(contacts)
 #   return index


#def test_emails_on_home_page(app, db):
#    #index = random(app)
#    contact_from_home_page = app.contact.get_contacts_list()
#    contact_from_db = db.get_contacts_list()
#    all_emails_from_home_page = contact_from_home_page.all_emails_from_home_page
#    assert sorted(all_emails_from_home_page, key=Contact.id_or_max) == \
#           sorted(merge_emails_like_on_home_page(contact_from_db), key=Contact.id_or_max)


#def test_phones_on_home_page(app):
#    index = random(app)
#    contact_from_home_page = app.contact.get_contacts_list()[index]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#    assert contact_from_home_page.all_tels_from_home_page == merge_tels_like_on_home_page(contact_from_edit_page)


#def clear(s):
#    return re.sub("[() -]", "", s)


#def merge_emails_like_on_home_page(db):
#    return "\n".join(filter(lambda x: x != "",
#                     map(lambda x: clear(x), filter(lambda x: x is not None,
#                                                    [db.get_contacts_list.email, db.get_contacts_list.email2,
#                                                     db.get_contacts_list.email3]))))


#def merge_tels_like_on_home_page(contact):
#    return "\n".join(filter(lambda x: x != "",
#                            map(lambda x: clear(x),
#                                filter(lambda x: x is not None,
#                                       [contact.home_tel, contact.mobile, contact.work_tel, contact.phone2]))))



