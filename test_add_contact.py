# -*- coding: utf-8 -*-
import pytest
import unittest, time, re
from contact import Contact
from application_contact import Application_contact

@pytest.fixture()
def app(request):
    fixture = Application_contact()
    request.addfinallizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname=u"Александр", middlename=u"Сергеевич", lastname=u"Пушкин", company=u"Царско-сельский лицей", address=u"г. Санкт-Петербург",
                             work_tel="1234567", e_mail="pushkin.as@gmail.com", bday="6", bmonth="June", byear="1799", address2="fhdkhgdk", notes="jfjhflf"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="", middlename="", lastname="", company="", address="", work_tel="", e_mail="", bday="-", bmonth="-", byear="", address2="", notes=""))
    app.logout()
