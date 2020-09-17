from selenium.webdriver.common.by import By

from web.pages.address_book.import_address_book import ImportAddressBook
from web.pages.base import Base
from web.pages.address_book.index import AddressBook
from web.pages.app_management.index import AppManagement
from web.pages.customer_contact.add_member import AddMember
from web.pages.customer_contact.index import CustomerContact
from web.pages.management_tools.attendance import Attendance
from web.pages.management_tools.group_message import GroupMessage
from web.pages.management_tools.index import ManagementTools
from web.pages.management_tools.members_join import MembersJoin
from web.pages.my_company.index import MyCompany


class Home(Base):
    # 进入顶部各菜单栏
    def goto_address_book(self):
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        return AddressBook(self._driver)

    def goto_app_management(self):
        self.find(By.CSS_SELECTOR, '#menu_apps').click()
        return AppManagement(self._driver)

    def goto_customer_contact(self):
        self.find(By.CSS_SELECTOR, '#menu_customer').click()
        return CustomerContact(self._driver)

    def goto_management_tools(self):
        self.find(By.CSS_SELECTOR, '#menu_manageTools').click()
        return ManagementTools(self._driver)

    def goto_my_company(self):
        self.find(By.CSS_SELECTOR, '#menu_profile').click()
        return MyCompany(self._driver)

    # 常用入口
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember(self._driver)

    def goto_import_address_book(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        return ImportAddressBook(self._driver)

    def goto_members_join(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(3)').click()
        return MembersJoin(self._driver)

    def goto_group_message(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(4)').click()
        return GroupMessage(self._driver)

    def goto_customer_contact2(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(5)').click()
        return CustomerContact(self._driver)

    def goto_attendance(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(6)').click()
        return Attendance(self._driver)