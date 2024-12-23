from pages.basePage import BasePage
from pages.page_home import HomePage


def test_small_room_one_hour(setup):
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")
    base_page.take_full_page_screenshot("E:\\Offline_Batch_20\\Projects\\Automation_Framework_20\\screenshots\\1_URL_open.png")
    home_page = HomePage(setup)
    home_page.select_room("Small Room")
    home_page.set_start_time("12", "12", "2024", "12", "00", "PM")
    base_page.take_screenshot("E:\\Offline_Batch_20\\Projects\\Automation_Framework_20\\screenshots\\2_set_start_time"
                              ".png")
    home_page.set_end_time("12", "12", "2024", "01", "00", "PM")
    base_page.take_screenshot(
        "E:\\Offline_Batch_20\\Projects\\Automation_Framework_20\\screenshots\\3_set_end_time.png")

    home_page.click_room_book_button()
    base_page.take_full_page_screenshot(
        "E:\\Offline_Batch_20\\Projects\\Automation_Framework_20\\screenshots\\4_actual_cost_small_one_hour.png")

    # Verify cost
    expected_cost_for_one_hour = "Total Cost: $100"

    # Call the method to get the actual booking cost
    actual_booking_cost_for_one_hour = home_page.get_actual_booking_cost()

    # Now use the actual cost for comparison in the assertion
    assert expected_cost_for_one_hour == actual_booking_cost_for_one_hour, \
        f"Test Case Failed. Expected Cost: {expected_cost_for_one_hour}, But Found: {actual_booking_cost_for_one_hour}"

    print("Test Case Passed. Cost for one hour is $100")


def test_small_room_three_hour(setup):
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")

    home_page = HomePage(setup)
    home_page.select_room("Small Room")
    home_page.set_start_time("12", "12", "2024", "12", "00", "PM")
    home_page.set_end_time("12", "12", "2024", "03", "00", "PM")

    home_page.click_room_book_button()

    # Verify cost
    expected_cost_for_one_hour = "Total Cost: $300"

    # Call the method to get the actual booking cost
    actual_booking_cost_for_one_hour = home_page.get_actual_booking_cost()

    # Now use the actual cost for comparison in the assertion
    assert expected_cost_for_one_hour == actual_booking_cost_for_one_hour, \
        f"Test Case Failed. Expected Cost: {expected_cost_for_one_hour}, But Found: {actual_booking_cost_for_one_hour}"

    print("Test Case Passed. Cost for one hour is $300")


def test_small_room_five_hour(setup):
    base_page = BasePage(setup)
    base_page.navigate_to_url("https://muntasir101.github.io/Conference-Room-Booking/")

    home_page = HomePage(setup)
    home_page.select_room("Small Room")
    home_page.set_start_time("12", "12", "2024", "12", "00", "PM")
    home_page.set_end_time("12", "12", "2024", "05", "00", "PM")

    home_page.click_room_book_button()

    # Verify cost
    expected_cost_for_one_hour = "Total Cost: $500"

    # Call the method to get the actual booking cost
    actual_booking_cost_for_one_hour = home_page.get_actual_booking_cost()

    # Now use the actual cost for comparison in the assertion
    assert expected_cost_for_one_hour == actual_booking_cost_for_one_hour, \
        f"Test Case Failed. Expected Cost: {expected_cost_for_one_hour}, But Found: {actual_booking_cost_for_one_hour}"

    print("Test Case Passed. Cost for one hour is $500")
