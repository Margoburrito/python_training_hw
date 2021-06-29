from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/"):
            return
        wd.find_element_by_link_text("home").click()

    def add_new(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # fill a contact's data
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def add_to_group(self, contact, group):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group.id)
        wd.find_element_by_name("add").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_value("firstname", contact.firstname)
        self.change_value("middlename", contact.middlename)
        self.change_value("lastname", contact.lastname)
        self.change_value("company", contact.company)
        self.change_value("address", contact.address)
        self.change_value("home", contact.home_tel)
        self.change_value("mobile", contact.mobile)
        self.change_value("work", contact.work_tel)
        self.change_value("email", contact.email)
        self.change_value("email2", contact.email2)
        self.change_value("email3", contact.email3)
        self.change_value("byear", contact.byear)
        self.change_value("address2", contact.address2)
        self.change_value("phone2", contact.phone2)
        self.change_value("notes", contact.notes)
        self.contact_form_select("bday", contact.bday)
        self.contact_form_select("bmonth", contact.bmonth)

    def contact_form_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_contact_worktel(self, index):
        self.select_contact_for_edit_by_index(0)

    def edit_contact_worktel_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_for_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_for_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()

    def select_contact_for_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("(//a[@href='edit.php?id=%s'])" % id).click()

    def edit_contact_name(self, index):
        self.select_contact_for_edit_by_index(0)

    def edit_contact_name_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_for_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_name_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_for_edit_by_id(id)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_tels = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_tels_from_home_page=all_tels))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_for_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_tel = wd.find_element_by_name("home").get_attribute("value")
        work_tel = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, email=email, email2=email2,
                       email3=email3, home_tel=home_tel, work_tel=work_tel, mobile=mobile, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_xpath("(//img[@alt='Details'])")[index].click()
        text = wd.find_element_by_id("content").text
        home_tel = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work_tel = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_tel=home_tel, work_tel=work_tel, mobile=mobile, phone2=phone2)
