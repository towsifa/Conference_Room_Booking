from pages.basePage import BasePage
from pages.page_home import HomePage


def test_medium_room_one_hour(setup):
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")

    home_page = HomePage(setup)
    home_page.select_room("Medium Room")
    home_page.set_start_time("12", "12", "2024", "12", "00", "PM")
    home_page.set_end_time("12", "12", "2024", "01", "00", "PM")

    home_page.click_room_book_button()

    # Verify cost
    expected_cost_for_one_hour = "Total Cost: $150"

    # Call the method to get the actual booking cost
    actual_booking_cost_for_one_hour = home_page.get_actual_booking_cost()

    # Now use the actual cost for comparison in the assertion
    assert expected_cost_for_one_hour == actual_booking_cost_for_one_hour, \
        f"Test Case Failed. Expected Cost: {expected_cost_for_one_hour}, But Found: {actual_booking_cost_for_one_hour}"

    print(f"Test Case Passed. Cost for one hour is :{expected_cost_for_one_hour}")


def test_medium_room_three_hour(setup):
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")

    home_page = HomePage(setup)
    home_page.select_room("Medium Room")
    home_page.set_start_time("12", "12", "2024", "12", "00", "PM")
    home_page.set_end_time("12", "12", "2024", "03", "00", "PM")

    home_page.click_room_book_button()

    # Verify cost
    expected_cost_for_one_hour = "Total Cost: $450"

    # Call the method to get the actual booking cost
    actual_booking_cost_for_one_hour = home_page.get_actual_booking_cost()

    # Now use the actual cost for comparison in the assertion
    assert expected_cost_for_one_hour == actual_booking_cost_for_one_hour, \
        f"Test Case Failed. Expected Cost: {expected_cost_for_one_hour}, But Found: {actual_booking_cost_for_one_hour}"

    print(f"Test Case Passed. Cost for one hour is :{expected_cost_for_one_hour}")


def test_medium_room_five_hour(setup):
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")

    home_page = HomePage(setup)
    home_page.select_room("Medium Room")
    home_page.set_start_time("12", "12", "2024", "12", "00", "PM")
    home_page.set_end_time("12", "12", "2024", "05", "00", "PM")

    home_page.click_room_book_button()

    # Verify cost
    expected_cost_for_one_hour = "Total Cost: $750"

    # Call the method to get the actual booking cost
    actual_booking_cost_for_one_hour = home_page.get_actual_booking_cost()

    # Now use the actual cost for comparison in the assertion
    assert expected_cost_for_one_hour == actual_booking_cost_for_one_hour, \
        f"Test Case Failed. Expected Cost: {expected_cost_for_one_hour}, But Found: {actual_booking_cost_for_one_hour}"

    print(f"Test Case Passed. Cost for one hour is :{expected_cost_for_one_hour}")
