import pytest
import yaml

from app.pages.app import App


class TestContact():
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().goto_home()
        self.invite_menu = self.main.goto_address_book().goto_member_invite_menu()

    @pytest.mark.parametrize("name, sex, mobile", yaml.safe_load(open("../datas/contact.yml", encoding="utf-8")))
    def test_add_member(self, name, sex, mobile):
        self.member_invit = self.invite_menu.goto_contact_add().contact_add(name, sex, mobile)
        assert "成功" in self.member_invit.get_toast()
