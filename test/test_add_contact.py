# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.add_new(Contact(firstname=u"Александр", middlename=u"Сергеевич", lastname=u"Пушкин", company=u"Царско-сельский лицей", address=u"г. Санкт-Петербург",
                                work_tel="1234567", e_mail="pushkin.as@gmail.com", bday="6", bmonth="June", byear="1799", address2="fhdkhgdk", notes="jfjhflf"))


def test_add_empty_contact(app):
    app.contact.add_new(Contact(firstname="", middlename="", lastname="", company="", address="", work_tel="", e_mail="", bday="-", bmonth="-", byear="", address2="", notes=""))
