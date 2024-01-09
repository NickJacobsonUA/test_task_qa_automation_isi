from selenium.webdriver.common.by import By


class AlertPageLocators:
    # Fill the Form
    ADD_ALERT_BUTTON = (By.CSS_SELECTOR, 'div[class="pull-right cursor-pointer color new-design-plus"]')
    NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    TEMPERATURE_FROM_F_INPUT = (By.CSS_SELECTOR, 'input[name="alert_from"]')
    TEMPERATURE_TO_F_INPUT = (By.CSS_SELECTOR, 'input[name="alert_to"]')
    SEND_SMS_TOGGLE = (By.XPATH, '//ng-form/div/div/div/div[4]/label/span/i')
    SEND_EMAIL_TOGGLE = (By.XPATH, '//ng-form/div/div/div/div[5]/label/span/i')
    AVAILABLE_LOCATIONS_OPTION = (By.CSS_SELECTOR, 'div[class="text-left item-li m15 p10"]')
    ADDED_LOCATIONS_OPTION = (By.CSS_SELECTOR, 'div[class="text-left item-li hover m15 p10"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-lg mr5 ml5 btn-success"]')
    
    # RESULT
    ADD_ALERT_RESULT = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope success clickable"]')

    # ALERT SEARCH
    ALERT_SEARCH = (By.XPATH, '//div/div[2]/div[2]/div/div/div[1]/div[1]/input')
    ALERT_SELECT = (By.CSS_SELECTOR, 'tr[class="thin-tr cursor-pointer ng-scope"] td[class="ng-binding"]~td[class="ng-binding"]')

    #Update result
    ALERT_UPDATE_RESULT = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope success clickable"]')

    # Invalid alert
    EMPTY_NAME = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope error clickable"]')
    TEMPERATURE_FROM_EMPTY = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope error clickable"]')
    ADDED_LOCATIONS_EMPTY = (By.CSS_SELECTOR, 'div[class="ui-notification ng-scope error clickable"]')




