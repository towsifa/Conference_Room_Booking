from pages.basePage import BasePage
from locators.homePageLocators import HomePageLocators
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    def select_room(self, value):
        self.select_dropdown_option_by_value(*HomePageLocators.Select_room, value)

    def set_start_time(self, month, day, year, hour, minute, am_pm=None):
        """
        Sets the start time by interacting with the datetime-local input field.

        :param month: The month to set (e.g., "12").
        :param day: The day to set (e.g., "20").
        :param year: The year to set (e.g., "2024").
        :param hour: The hour to set (e.g., "12").
        :param minute: The minute to set (e.g., "30").
        :param am_pm: Optional. AM/PM format ("AM" or "PM"). If not provided, 24-hour time will be used.
        """
        # Convert hour and minute to 24-hour time if AM/PM is provided
        hour = int(hour)  # Ensure hour is integer
        if am_pm:
            am_pm = am_pm.upper()
            if am_pm == "AM" and hour == 12:
                hour = 0  # Midnight (12 AM)
            elif am_pm == "PM" and hour != 12:
                hour += 12  # Convert PM to 24-hour time

        # Format date-time string for input
        date_time_str = f"{month}-{day}-{year}T{str(hour).zfill(2)}:{minute}"

        # Input the formatted date-time string
        self.click_element(*HomePageLocators.Start_time)
        self.driver.find_element(*HomePageLocators.Start_time).clear()
        self.driver.find_element(*HomePageLocators.Start_time).send_keys(date_time_str)

    def set_end_time(self, month, day, year, hour, minute, am_pm=None):
        """
        Sets the start time by interacting with the datetime-local input field.

        :param month: The month to set (e.g., "12").
        :param day: The day to set (e.g., "20").
        :param year: The year to set (e.g., "2024").
        :param hour: The hour to set (e.g., "12").
        :param minute: The minute to set (e.g., "30").
        :param am_pm: Optional. AM/PM format ("AM" or "PM"). If not provided, 24-hour time will be used.
        """
        # Convert hour and minute to 24-hour time if AM/PM is provided
        hour = int(hour)  # Ensure hour is integer
        if am_pm:
            am_pm = am_pm.upper()
            if am_pm == "AM" and hour == 12:
                hour = 0  # Midnight (12 AM)
            elif am_pm == "PM" and hour != 12:
                hour += 12  # Convert PM to 24-hour time

        # Format date-time string for input
        date_time_str = f"{month}-{day}-{year}T{str(hour).zfill(2)}:{minute}"

        # Input the formatted date-time string
        self.click_element(*HomePageLocators.End_time)
        self.driver.find_element(*HomePageLocators.End_time).clear()
        self.driver.find_element(*HomePageLocators.End_time).send_keys(date_time_str)

    def click_room_book_button(self):
        self.click_element(*HomePageLocators.Book_room_button)

    def get_actual_booking_cost(self):
        return self.get_element_text(*HomePageLocators.Booking_cost)
