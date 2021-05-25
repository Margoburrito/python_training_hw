from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, company=None, address=None, home_tel=None, work_tel=None,
                 mobile=None, fax=None, e_mail=None, bday=None, bmonth=None, byear=None, address2=None,
                 all_tels_from_home_page=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.work_tel = work_tel
        self.mobile = mobile
        self.fax = fax
        self.e_mail = e_mail
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.all_tels_from_home_page = all_tels_from_home_page
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize