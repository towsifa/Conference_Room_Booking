from pages.basePage import BasePage


def test_home_open(setup):
    basePage = BasePage(setup)
    basePage.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")
