import re
from model.contact import Contact


def test_data_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contacts_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        contact_from_db[i] = like_home_page(contact_from_db[i])
        assert contact_from_home_page[i].id == contact_from_db[i].id
        assert contact_from_home_page[i].firstname == contact_from_db[i].firstname
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].all_emails_from_home_page == contact_from_db[i].all_emails_from_home_page
        assert contact_from_home_page[i].all_tels_from_home_page == contact_from_db[i].all_tels_from_home_page


def like_home_page(contact):
    return Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname,
                   address=contact.address, all_emails_from_home_page=merge_emails_like_on_home_page(contact),
                   all_tels_from_home_page=merge_tels_like_on_home_page(contact))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x), filter(lambda x: x is not None,
                                                    [contact.email, contact.email2,
                                                     contact.email3]))))


def merge_tels_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_tel, contact.mobile, contact.work_tel, contact.phone2]))))



