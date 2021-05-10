from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # fill a contact's data
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_value("firstname", contact.firstname)
        self.change_value("middlename", contact.middlename)
        self.change_value("lastname", contact.lastname)
        self.change_value("company", contact.company)
        self.change_value("address", contact.address)
        self.change_value("work", contact.work_tel)
        self.change_value("email", contact.e_mail)
        self.change_value("byear", contact.byear)
        self.change_value("address2", contact.address2)
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
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_name("selected[]")

    def edit_contact_worktel(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def edit_contact_name(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

