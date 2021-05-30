from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, company=None, address=None, home_tel=None,
                 work_tel=None, mobile=None, fax=None, email=None, email2=None, email3=None, all_emails_from_home_page=None, bday=None, bmonth=None,
                 byear=None, address2=None, all_tels_from_home_page=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.work_tel = work_tel
        self.mobile = mobile
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.all_tels_from_home_page = all_tels_from_home_page
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address, self.email,
                                                     self.email2, self.email3, self.home_tel, self.mobile, self.work_tel,
                                                     self.phone2)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize