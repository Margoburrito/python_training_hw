from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_second_contact(Contact(firstname=u"Михаил", middlename=u"Юрьевич", lastname=u"Лермонтов", company="", address=u"г. Пятигорск",
                                            work_tel="897654", e_mail="lermontov.mu@gmail.com", bday="15", bmonth="October", byear="1814", address2="Машук", notes="дуэль"))