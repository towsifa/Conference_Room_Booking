from selenium.common import TimeoutException, NoSuchWindowException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """
        Initializes a new instance of the BasePage class.

        Parameters:
            driver (WebDriver): The Selenium WebDriver instance for browser automation.
        """
        self.driver = driver

    def navigate_to_url(self, url):
        """
        Navigates to the specified URL.

        Parameters:
            url (str): The URL to navigate to.
        """
        self.driver.get(url)

    def get_cookie(self, cookie_name):
        """
        Retrieves the value of the specified cookie.

        Parameters:
            cookie_name (str): The name of the cookie.

        Returns:
            dict or None: The dictionary representing the cookie if found, or None if not found.
        """
        return self.driver.get_cookie(cookie_name)

    def get_all_cookies(self):
        """
        Retrieves all cookies present in the current browser session.

        Returns:
            list[dict]: A list of dictionaries representing all cookies.
        """
        return self.driver.get_cookies()

    def add_cookie(self, cookie_dict):
        """
        Adds a new cookie to the browser session.

        Parameters:
            cookie_dict (dict): A dictionary representing the cookie to be added.
        """
        self.driver.add_cookie(cookie_dict)

    def delete_cookie(self, cookie_name):
        """
        Deletes the specified cookie from the browser session.

        Parameters:
            cookie_name (str): The name of the cookie to be deleted.
        """
        self.driver.delete_cookie(cookie_name)

    def delete_all_cookies(self):
        """
        Deletes all cookies from the current browser session.
        """
        self.driver.delete_all_cookies()

    def minimize_window(self):
        """
        Minimizes the current browser window.

        Usage:
            base_page.minimize_window()
        """
        self.driver.minimize_window()

    def set_window_size(self, width, height):
        """
        Sets the size of the current browser window.

        Parameters:
            width (int): The desired width of the window.
            height (int): The desired height of the window.

        Usage:
            base_page.set_window_size(1200, 800)
        """
        self.driver.set_window_size(width, height)

    def get_current_window_size(self):
        """
        Retrieves the size of the current browser window.

        Returns:
            dict: A dictionary with 'width' and 'height' keys representing the window size.

        Usage:
            window_size = base_page.get_current_window_size()
        """
        return self.driver.get_window_size()

    def get_current_window_position(self):
        """
        Retrieves the position of the current browser window.

        Returns:
            dict: A dictionary with 'x' and 'y' keys representing the window position.

        Usage:
            window_position = base_page.get_current_window_position()
        """
        return self.driver.get_window_position()

    def wait_for_element(self, by, value, timeout=10):
        """
        Waits for the presence of an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.CSS, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            timeout (int): The maximum time to wait for the element (default is 10 seconds).

        Returns:
            WebElement: The located WebElement.

        Usage:
            element = base_page.wait_for_element(By.ID, 'exampleId')
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def get_element_location(self, by, value):
        """
        Retrieves the location of an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            dict: A dictionary with 'x' and 'y' keys representing the location.

        Usage:
            location = base_page.get_element_location(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        return element.location

    def get_element_size(self, by, value):
        """
        Retrieves the size of an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            dict: A dictionary with 'width' and 'height' keys representing the size.

        Usage:
            size = base_page.get_element_size(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        return element.size

    def click_element(self, by, value):
        """
        Waits for the presence of an element and then clicks it.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.click_element(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        element.click()

    def type_text(self, by, value, text):
        """
        Waits for the presence of an element, clears its content, and inputs the specified text.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            text: The text to input into the element.

        Usage:
            base_page.input_text(By.ID, 'exampleId', 'Hello, World!')
        """
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def wait_for_visible_element(self, by, value, timeout=10):
        """
        Waits for the visibility of an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            timeout (int): The maximum time to wait for the element to be visible (default is 10 seconds).

        Returns:
            WebElement: The located WebElement.

        Usage:
            element = base_page.wait_for_visible_element(By.ID, 'exampleId')
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def wait_for_invisible_element(self, by, value, timeout=10):
        """
        Waits for the invisibility of an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            timeout (int): The maximum time to wait for the element to be invisible (default is 10 seconds).

        Returns:
            bool: True if the element becomes invisible within the specified timeout, False otherwise.

        Usage:
            is_invisible = base_page.wait_for_invisible_element(By.ID, 'exampleId')
        """
        return WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located((by, value)))

    def get_element_text(self, by, value):
        """
        Retrieves the text content of an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            str: The text content of the element.

        Usage:
            text_content = base_page.get_element_text(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        return element.text

    def get_element_attribute(self, by, value, attribute):
        """
        Retrieves the value of a specified attribute of an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            attribute: The name of the attribute whose value is to be retrieved.

        Returns:
            str or None: The value of the specified attribute, or None if the attribute is not present.

        Usage:
            attribute_value = base_page.get_element_attribute(By.ID, 'exampleId', 'class')
        """
        element = self.wait_for_element(by, value)
        return element.get_attribute(attribute)

    def select_dropdown_option_by_visible_text(self, by, value, option_text):
        """
        Waits for the presence of a dropdown element, selects an option by visible text.

        Parameters:
            by: The method used to locate the dropdown element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the dropdown element.
            option_text: The visible text of the option to be selected.

        Usage:
            base_page.select_dropdown_option_by_visible_text(By.ID, 'exampleDropdown', 'Option 1')
        """
        element = self.wait_for_element(by, value)
        select = Select(element)
        select.select_by_visible_text(option_text)

    def select_dropdown_option_by_value(self, by, value, option_value):
        """
        Waits for the presence of a dropdown element and selects an option by its value.

        Parameters:
            by: The method used to locate the dropdown element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the dropdown element.
            option_value: The value of the option to be selected.

        Usage:
            base_page.select_dropdown_option_by_value(By.ID, 'exampleDropdown', 'optionValue1')
        """
        element = self.wait_for_element(by, value)
        select = Select(element)
        select.select_by_value(option_value)

    def get_selected_option_text(self, by, value):
        """
        Retrieves the text of the currently selected option in a dropdown element.

        Parameters:
            by: The method used to locate the dropdown element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the dropdown element.

        Returns:
            str: The text of the currently selected option.

        Usage:
            selected_text = base_page.get_selected_option_text(By.ID, 'exampleDropdown')
        """
        element = self.wait_for_element(by, value)
        select = Select(element)
        return select.first_selected_option.text

    def is_element_displayed(self, by, value):
        """
        Checks if an element identified by the specified method and value is displayed on the page.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            bool: True if the element is displayed, False otherwise.

        Usage:
            is_displayed = base_page.is_element_displayed(By.ID, 'exampleId')
        """
        try:
            element = self.wait_for_visible_element(by, value)
            return element.is_displayed()
        except TimeoutException:
            return False

    def is_element_clickable(self, by, value, timeout=10):
        """
        Checks if an element identified by the specified method and value is clickable within a specified timeout.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            timeout (int): The maximum time to wait for the element to be clickable (default is 10 seconds).

        Returns:
            bool: True if the element is clickable, False otherwise.

        Usage:
            is_clickable = base_page.is_element_clickable(By.ID, 'exampleId', timeout=5)
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return True
        except TimeoutException:
            return False

    def is_element_enabled(self, by, value):
        """
        Checks if an element identified by the specified method and value is enabled.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            bool: True if the element is enabled, False otherwise.

        Usage:
            is_enabled = base_page.is_element_enabled(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        return element.is_enabled()

    def is_element_selected(self, by, value):
        """
        Checks if an element identified by the specified method and value is selected.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            bool: True if the element is selected, False otherwise.

        Usage:
            is_selected = base_page.is_element_selected(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        return element.is_selected()

    def get_page_title(self):
        """
        Retrieves the title of the current page.

        Returns:
            str: The title of the current page.

        Usage:
            page_title = base_page.get_page_title()
        """
        return self.driver.title

    def get_current_url(self):
        """
        Retrieves the current URL of the browser.

        Returns:
            str: The current URL.

        Usage:
            current_url = base_page.get_current_url()
        """
        return self.driver.current_url

    def get_current_page_url(self):
        """
        Retrieves the current page URL. Alias for get_current_url.

        Returns:
            str: The current page URL.

        Usage:
            current_page_url = base_page.get_current_page_url()
        """
        return self.driver.current_url

    def navigate_back(self):
        """
        Navigates the browser back one page.

        Usage:
            base_page.navigate_back()
        """
        self.driver.back()

    def navigate_forward(self):
        """
        Navigates the browser forward one page.

        Usage:
            base_page.navigate_forward()
        """
        self.driver.forward()

    def refresh_page(self):
        """
        Refreshes the current page.

        Usage:
            base_page.refresh_page()
        """
        self.driver.refresh()

    def switch_to_frame(self, by, value):
        """
        Switches the focus to a frame identified by the specified method and value.

        Parameters:
            by: The method used to locate the frame (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the frame.

        Usage:
            base_page.switch_to_frame(By.ID, 'frameId')
        """
        frame = self.wait_for_element(by, value)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        """
        Switches the focus back to the default content.

        Usage:
            base_page.switch_to_default_content()
        """
        self.driver.switch_to.default_content()

    def execute_script(self, script, *args):
        """
        Executes JavaScript in the context of the current page.

        Parameters:
            script (str): The JavaScript code to execute.
            *args: Arguments to pass to the JavaScript code.

        Returns:
            Any: The result of the executed JavaScript.

        Usage:
            result = base_page.execute_script("return document.title;")
        """
        return self.driver.execute_script(script, *args)

    def perform_keyboard_shortcut(self, *keys):
        """
        Performs a keyboard shortcut using the specified keys.

        Parameters:
            *keys: The keys to press for the shortcut.

        Usage:
            base_page.perform_keyboard_shortcut(Keys.CONTROL, 'a')  # Example: Select all
        """
        actions = ActionChains(self.driver)
        actions.send_keys(*keys).perform()

    def hover_over_element(self, by, value):
        """
        Hovers the mouse over an element identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.hover_over_element(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def drag_and_drop(self, source_by, source_value, target_by, target_value):
        """
        Drags an element identified by the source method and value and drops it onto another element identified
        by the target method and value.

        Parameters:
            source_by: The method used to locate the source element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            source_value: The value of the method identifying the source element.
            target_by: The method used to locate the target element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            target_value: The value of the method identifying the target element.

        Usage:
            base_page.drag_and_drop(By.ID, 'sourceId', By. ID, 'targetId')
        """
        source_element = self.wait_for_element(source_by, source_value)
        target_element = self.wait_for_element(target_by, target_value)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def capture_screenshot(self, filename):
        """
        Captures a screenshot of the current page and saves it to the specified filename.

        Parameters:
            filename (str): The filename (with path) to save the screenshot.

        Usage:
            base_page.capture_screenshot("path/to/screenshot.png")
        """
        self.driver.save_screenshot(filename)

    def close_browser(self):
        """
        Closes the browser.

        Usage:
            base_page.close_browser()
        """
        self.driver.close()

    def quit_browser(self):
        """
        Closes the browser.

        Usage:
            base_page.quit_browser()
        """
        self.driver.quit()

    def wait_for_alert(self, timeout=10):
        """
        Waits for an alert to be present within the specified timeout and returns the Alert object.

        Parameters:
            timeout (int): The maximum time to wait for the alert (default is 10 seconds).

        Returns:
            Alert: The Alert object.

        Usage:
            alert = base_page.wait_for_alert()
        """
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    def wait_for_alert_to_be_present(self, timeout=10):
        """
        Waits for an alert to be present.

        Parameters:
            timeout (int): The maximum time to wait for the condition (default is 10 seconds).

        Usage:
            base_page.wait_for_alert_to_be_present(timeout=15)
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.alert_is_present()
        )

    def switch_to_alert(self):
        """
        Switches the focus to the current alert and returns the Alert object.

        Returns:
            Alert: The Alert object.

        Usage:
            alert = base_page.switch_to_alert()
        """
        return self.driver.switch_to.alert

    def accept_alert(self):
        """
        Accepts the current alert.

        Usage:
            base_page.accept_alert()
        """
        alert = self.wait_for_alert()
        alert.accept()

    def get_alert_text(self):
        """
        Retrieves the text of the current alert.

        Returns:
            str: The text of the alert.

        Usage:
            alert_text = base_page.get_alert_text()
        """
        alert = self.wait_for_alert()
        return alert.text

    def switch_to_frame_by_index(self, frame_index):
        """
        Switches the focus to a frame using its index.

        Parameters:
            frame_index (int): The index of the frame to switch to.

        Usage:
            base_page.switch_to_frame_by_index(0)
        """
        self.driver.switch_to.frame(frame_index)

    def switch_to_frame_by_name_or_id(self, frame_name_or_id):
        """
        Switches the focus to a frame using its name or ID.

        Parameters:
            frame_name_or_id (str): The name or ID of the frame to switch to.

        Usage:
            base_page.switch_to_frame_by_name_or_id('exampleFrame')
        """
        self.driver.switch_to.frame(frame_name_or_id)

    def switch_to_parent_frame(self):
        """
        Switches the focus back to the parent frame.

        Usage:
            base_page.switch_to_parent_frame()
        """
        self.driver.switch_to.parent_frame()

    def switch_to_window(self, window_handle):
        """
        Switches the focus to a window with the specified window handle.

        Parameters:
            window_handle (str): The window handle to switch to.

        Usage:
            base_page.switch_to_window('exampleHandle')
        """
        self.driver.switch_to.window(window_handle)

    def get_all_window_handles(self):
        """
        Retrieves a list of all window handles.

        Returns:
            List[str]: A list of window handles.

        Usage:
            window_handles = base_page.get_all_window_handles()
        """
        return self.driver.window_handles

    def get_current_window_handle(self):
        """
        Retrieves the handle of the current window.

        Returns:
            str: The handle of the current window.

        Usage:
            current_window_handle = base_page.get_current_window_handle()
        """
        return self.driver.current_window_handle

    def switch_to_window_by_index(self, window_index):
        """
        Switches the focus to a window using its index.

        Parameters:
            window_index (int): The index of the window to switch to.

        Raises:
            IndexError: If the specified window index is out of range.

        Usage:
            base_page.switch_to_window_by_index(0)
        """
        window_handles = self.driver.window_handles
        if window_index < len(window_handles):
            self.driver.switch_to.window(window_handles[window_index])
        else:
            raise IndexError(f"Window index {window_index} is out of range.")

    def switch_to_window_by_title(self, window_title):
        """
        Switches the focus to a window with the specified title.

        Parameters:
            window_title (str): The title of the window to switch to.

        Raises:
            NoSuchWindowException: If no window with the specified title is found.

        Usage:
            base_page.switch_to_window_by_title('Example Window Title')
        """
        current_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                if window_title in self.driver.title:
                    return
        raise NoSuchWindowException(f"No window with title '{window_title}' found.")

    def switch_to_window_by_url(self, window_url):
        """
        Switches the focus to a window with the specified URL.

        Parameters:
            window_url (str): The URL of the window to switch to.

        Raises:
            NoSuchWindowException: If no window with the specified URL is found.

        Usage:
            base_page.switch_to_window_by_url('http://example.com')
        """
        current_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                if window_url in self.driver.current_url:
                    return
        raise NoSuchWindowException(f"No window with URL '{window_url}' found.")

    def scroll_into_view(self, by, value):
        """
        Scrolls the page to bring the specified element into view.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.scroll_into_view(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def perform_double_click(self, by, value):
        """
        Performs a double click on the specified element.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.perform_double_click(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def perform_right_click(self, by, value):
        """
        Performs a right-click on the specified element.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.perform_right_click(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def upload_file(self, by, value, file_path):
        """
        Uploads a file to the specified input element.

        Parameters:
            by: The method used to locate the input element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the input element.
            file_path: The path to the file to be uploaded.

        Usage:
            base_page.upload_file(By.ID, 'fileInput', '/path/to/file.txt')
        """
        element = self.wait_for_element(by, value)
        element.send_keys(file_path)

    def download_file(self, url, destination_path):
        """
        Downloads a file from the given URL to the specified destination path.

        Parameters:
            url (str): The URL of the file to download.
            destination_path (str): The path where the downloaded file should be saved.

        Usage:
            base_page.download_file('http://example.com/file.zip', '/path/to/save/file.zip')
        """
        # Code to download a file from a URL to a specified destination path
        # This might involve using the 'requests' library or other appropriate method
        pass

    def wait_for_elements(self, by, value, timeout=10):
        """
        Waits for the presence of all elements identified by the specified method and value.

        Parameters:
            by: The method used to locate the elements (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            timeout (int): The maximum time to wait for the elements (default is 10 seconds).

        Returns:
            List[WebElement]: A list of WebElement objects representing the found elements.

        Usage:
            elements = base_page.wait_for_elements(By.CLASS_NAME, 'exampleClass')
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )

    def click_elements(self, by, value, index=None):
        """
        Clicks on one or multiple elements identified by the specified method and value.

        Parameters:
            by: The method used to locate the elements (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the elements.
            index (int or None): The index of the element to click (if multiple elements are found).

        Usage:
            base_page.click_elements(By.CLASS_NAME, 'exampleClass')
            base_page.click_elements(By.XPATH, '//button', index=0)
        """
        elements = self.wait_for_elements(by, value)
        if index is not None:
            elements[index].click()
        else:
            for element in elements:
                element.click()

    def get_element_count(self, by, value):
        """
        Retrieves the count of elements identified by the specified method and value.

        Parameters:
            by: The method used to locate the elements (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the elements.

        Returns:
            int: The count of elements.

        Usage:
            count = base_page.get_element_count(By.TAG_NAME, 'div')
        """
        elements = self.wait_for_elements(by, value)
        return len(elements)

    def execute_async_script(self, script, *args):
        """
        Executes asynchronous JavaScript in the context of the current page.

        Parameters:
            script (str): The JavaScript code to execute.
            *args: Arguments to pass to the JavaScript code.

        Returns:
            Any: The result of the executed JavaScript.

        Usage:
            result = base_page.execute_async_script("return someAsyncFunction();")
        """
        return self.driver.execute_async_script(script, *args)

    def get_page_source(self):
        """
        Retrieves the source code of the current page.

        Returns:
            str: The source code of the current page.

        Usage:
            page_source = base_page.get_page_source()
        """
        return self.driver.page_source

    def scroll_to_bottom(self):
        """
        Scrolls the page to the bottom.

        Usage:
            base_page.scroll_to_bottom()
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """
        Scrolls the page to the top.

        Usage:
            base_page.scroll_to_top()
        """
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_to_element(self, by, value):
        """
        Scrolls the page to bring the specified element into view.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.scroll_to_element(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def drag_and_drop_by_offset(self, by, value, x_offset, y_offset):
        """
        Drags an element identified by the specified method and value and drops it at the specified offset.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            x_offset (int): The horizontal offset for the drop.
            y_offset (int): The vertical offset for the drop.

        Usage:
            base_page.drag_and_drop_by_offset(By.ID, 'exampleId', 50, 50)
        """
        element = self.wait_for_element(by, value)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(element, x_offset, y_offset).perform()

    def press_enter_key(self, by, value):
        """
        Presses the Enter key on the specified element.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.press_enter_key(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        element.send_keys(Keys.ENTER)

    def press_tab_key(self, by, value):
        """
        Presses the Tab key on the specified element.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.press_tab_key(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        element.send_keys(Keys.TAB)

    def press_escape_key(self, by, value):
        """
        Presses the Escape key on the specified element.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Usage:
            base_page.press_escape_key(By.ID, 'exampleId')
        """
        element = self.wait_for_element(by, value)
        element.send_keys(Keys.ESCAPE)

    def take_screenshot(self, filename):
        """
        Takes a screenshot of the current page and saves it to the specified filename.

        Parameters:
            filename (str): The filename (with path) to save the screenshot.

        Usage:
            base_page.take_screenshot("path/to/screenshot.png")
        """
        self.driver.save_screenshot(filename)

    def get_dropdown_options(self, by, value):
        """
        Retrieves the options available in a dropdown identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).

        Returns:
            List[str]: A list of text values representing the dropdown options.

        Usage:
            options = base_page.get_dropdown_options(By.ID, 'exampleDropdown')
        """
        element = self.wait_for_element(by, value)
        select = Select(element)
        return [option.text for option in select.options]

    def select_multiple_dropdown_options(self, by, value, options):
        """
        Selects multiple options in a dropdown identified by the specified method and value.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            options (List[str]): A list of option texts to select.

        Usage:
            base_page.select_multiple_dropdown_options(By.ID, 'exampleDropdown', ['Option1', 'Option2'])
        """
        element = self.wait_for_element(by, value)
        select = Select(element)
        for option in options:
            select.select_by_visible_text(option)

    def get_attribute_value(self, by, value, attribute):
        """
        Retrieves the value of the specified attribute from the element.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            attribute (str): The name of the attribute to retrieve.

        Returns:
            str: The value of the specified attribute.

        Usage:
            value = base_page.get_attribute_value(By.ID, 'exampleId', 'data-custom-attribute')
        """
        element = self.wait_for_element(by, value)
        return element.get_attribute(attribute)

    def wait_for_url_to_contain(self, partial_url, timeout=10):
        """
        Waits for the URL to contain the specified partial URL.

        Parameters:
            partial_url (str): The partial URL to wait for.
            timeout (int): The maximum time to wait for the condition (default is 10 seconds).

        Usage:
            base_page.wait_for_url_to_contain('example', timeout=15)
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )

    def wait_for_url_to_match(self, full_url, timeout=10):
        """
        Waits for the URL to match the specified full URL.

        Parameters:
            full_url (str): The full URL to wait for.
            timeout (int): The maximum time to wait for the condition (default is 10 seconds).

        Usage:
            base_page.wait_for_url_to_match('http://example.com', timeout=15)
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(full_url)
        )

    def hover_and_click(self, hover_by, hover_value, click_by, click_value):
        """
        Hovers over an element and clicks another element.

        Parameters:
            hover_by: The method used to locate the hover element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            hover_value: The value of the method (e.g., the ID, name, or XPath expression) identifying the hover element.
            click_by: The method used to locate the click element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            click_value: The value of the method (e.g., the ID, name, or XPath expression) identifying the click element.

        Usage:
            base_page.hover_and_click(By.ID, 'hoverElementId', By.NAME, 'clickElementName')
        """
        hover_element = self.wait_for_element(hover_by, hover_value)
        click_element = self.wait_for_element(click_by, click_value)

        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).click(click_element).perform()

    def wait_for_text_to_be_present_in_element(self, by, value, text, timeout=10):
        """
        Waits for the specified text to be present in the identified element.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression).
            text: The text to wait for.
            timeout (int): The maximum time to wait for the condition (default is 10 seconds).

        Usage:
            base_page.wait_for_text_to_be_present_in_element(By.ID, 'exampleId', 'expectedText', timeout=15)
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((by, value), text)
        )

    def wait_for_text_to_be_present_in_element_value(self, by, value, text, timeout=10):
        """
        Waits for the specified text to be present in the value of the identified element.

        Parameters:
            by: The method used to locate the element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the element.
            text: The text to wait for.
            timeout (int): The maximum time to wait for the condition (default is 10 seconds).

        Usage:
            base_page.wait_for_text_to_be_present_in_element_value(By.ID, 'exampleId', 'expectedText', timeout=15)
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_value((by, value), text)
        )

    def upload_file_using_input(self, by, value, file_path):
        """
        Uploads a file to the specified input element using the input field.

        Parameters:
            by: The method used to locate the input element (e.g., By. ID, By.NAME, By.XPATH, etc.).
            value: The value of the method (e.g., the ID, name, or XPath expression) identifying the input element.
            file_path (str): The path to the file to be uploaded.

        Usage:
            base_page.upload_file_using_input(By.ID, 'fileInputId', '/path/to/file.txt')
        """
        element = self.wait_for_element(by, value)
        element.send_keys(file_path)

    def take_full_page_screenshot(self, filename):
        """
        Takes a full-page screenshot of the current page and saves it to the specified filename.

        Parameters:
            filename (str): The filename (with path) to save the screenshot.

        Usage:
            base_page.take_full_page_screenshot("path/to/fullpage_screenshot.png")
        """
        # Set window size to full page height dynamically
        page_width = self.driver.execute_script("return document.body.scrollWidth")
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.set_window_size(page_width, page_height)

        # Take the screenshot
        self.driver.save_screenshot(filename)