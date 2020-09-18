from web.pages.home.index import Home


class TestAddMemeber:
    def setup(self):
        self.home = Home()

    def test_add_member(self):
        # self.home.goto_add_member().add_member_save()
        adb = self.home.goto_address_book()
        adb.goto_add_member().add_member_save()
        assert adb.get_member_page("13000000002")

    def test_get_member(self):
        assert self.home.goto_address_book().get_member_search("13000000002")
