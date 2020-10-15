from app.pages.app import App


class TestContact():
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_home()

    def test_add_member(self):
        self.member_invit = self.main.goto_address_book().goto_member_invite_menu().goto_contact_add().contact_add()
        assert "成功" in self.member_invit.get_toast()
