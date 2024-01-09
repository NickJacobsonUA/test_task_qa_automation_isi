import allure

from generator.generator import generated_data
from locators.alerts_page_locators import AlertPageLocators
from pages.base_page import BasePage


class AddAlertPage(BasePage):
    locators = AlertPageLocators

    @allure.step('Filling the form to add an alert')
    def fill_add_alert_form(self):
        # generating data
        gen = next(generated_data())
        # interaction with the form
        self.element_is_visible(self.locators.ADD_ALERT_BUTTON).click()
        with allure.step('filling the fields'):
            self.element_is_visible(self.locators.NAME_INPUT).send_keys(gen.username)
            self.element_is_visible(self.locators.TEMPERATURE_FROM_F_INPUT).send_keys(gen.temperature_from)
            self.element_is_visible(self.locators.TEMPERATURE_TO_F_INPUT).send_keys(gen.temperature_to)
            self.element_is_visible(self.locators.AVAILABLE_LOCATIONS_OPTION).click()
        self.element_is_clickable(self.locators.ADDED_LOCATIONS_OPTION)
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        return gen.username

    @allure.step('Checking the result of adding an alert')
    def check_add_alert(self):
        with allure.step('getting the add alert message text'):
            result = self.element_is_present(self.locators.ADD_ALERT_RESULT).text
        # Clicking to have it gone
        self.element_is_present(self.locators.ADD_ALERT_RESULT).click()
        return result


class UpdateAlertPage(BasePage):
    locators = AlertPageLocators

    @allure.step('Changing the add allert form data to have it updated')
    def update_alert(self):
        name = self.element_is_present(self.locators.ALERT_SELECT).text
        self.element_is_present(self.locators.ALERT_SELECT).click()
        with allure.step('Switching the toggle Email'):
            self.element_is_visible(self.locators.SEND_EMAIL_TOGGLE).click()
        self.element_is_visible(self.locators.SAVE_BUTTON).click()
        return name

    @allure.step('Checking the result of updating')
    def check_update_alert(self):
        with allure.step('getting the update alert message text'):
            result = self.element_is_present(self.locators.ALERT_UPDATE_RESULT).text
        # Clicking to have it gone
        self.element_is_present(self.locators.ALERT_UPDATE_RESULT).click()
        return result


class InvalidAlertPage(BasePage):
    locators = AlertPageLocators

    @allure.step('Check adding an invalid alert')
    def add_invalid_alert(self):
        gen = next(generated_data())
        self.element_is_visible(self.locators.ADD_ALERT_BUTTON).click()
        with allure.step('Filling the add alert form not completely'):
            self.element_is_clickable(self.locators.NAME_INPUT).send_keys(gen.username)
            self.element_is_visible(self.locators.TEMPERATURE_FROM_F_INPUT).send_keys(gen.temperature_from)
            self.element_is_visible(self.locators.TEMPERATURE_TO_F_INPUT).send_keys(gen.temperature_to)
            self.element_is_visible(self.locators.SAVE_BUTTON).click()
        with allure.step('getting the update alert message text'):
            result = self.element_is_present(self.locators.EMPTY_NAME).text
            return [result]







