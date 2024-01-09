import allure
from pages.alerts_page import AddAlertPage, UpdateAlertPage, InvalidAlertPage
from conftest import driver


@allure.suite("Alerts")
class TestAlerts:

    @allure.title('Check Add Alert')
    def test_add_new_alert(self, driver):
        add_alert = AddAlertPage(driver, "https://test-hg.isi-technology.com/#!/alert")
        add_alert.open()
        user = add_alert.fill_add_alert_form()
        result = add_alert.check_add_alert()
        print(result)
        assert result == f'{user} was created.', 'The alert was not created'

    @allure.title('Check Update Alert')
    def test_update_alert(self, driver):
        update_alert = UpdateAlertPage(driver, "https://test-hg.isi-technology.com/#!/alert")
        update_alert.open()
        user = update_alert.update_alert()
        result = update_alert.check_update_alert()
        print(result)
        assert result == f'{user} was updated.', 'The alert was not updated'

    @allure.title('Check adding an Invalid Alert')
    def test_add_invalid_alert(self, driver):
        invalid = InvalidAlertPage(driver, "https://test-hg.isi-technology.com/#!/alert")
        invalid.open()
        result = invalid.add_invalid_alert()
        assert any(item in result for item in (
        'This field may not be blank.', 'A valid number is required.', 'This field is required.',
        'This list may not be empty.')), 'The user was created'

