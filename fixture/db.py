import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, user=user, password=password, database=name, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, home_tel=home,
                                    mobile=mobile, work_tel=work, phone2=phone2, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_groups_with_contacts(self):
        list = []

        with self.connection.cursor() as cursor:
            cursor.execute("select distinct(group_id), 'dummy' from address_in_groups where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (group_id, dummy) = row
                list.append(Group(id=str(group_id)))
        return list

    def destroy(self):
        self.connection.close()

